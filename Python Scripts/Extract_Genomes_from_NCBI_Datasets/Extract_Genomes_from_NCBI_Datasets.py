import subprocess
from pathlib import Path
import zipfile
import pandas as pd
from tqdm import tqdm
import json

OUTPUT_DIR = Path("Output_Genomes")
CSV_FILE = Path("genbank_assemblies_by_taxon.csv")

df = pd.read_csv(CSV_FILE)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_path)

def get_assembly_level_from_jsonl(folder_path):

    jsonl_dir = folder_path / "ncbi_dataset" / "data"
    jsonl_files = list(jsonl_dir.glob("*.jsonl"))
    if not jsonl_files:
        return "Unknown"
    with open(jsonl_files[0], "r") as f:
        data = json.load(f)
    return data.get("assemblyInfo", {}).get("assemblyLevel", "Unknown").replace(" ", "_")

def rename_fna_files(folder_path, assembly_accession, assembly_level):

    for fna_file in folder_path.glob("*.fna"):
        new_name = f"{assembly_accession}_{assembly_level}.fna"
        new_path = fna_file.parent / new_name
        fna_file.rename(new_path)

total_genomes = len(df)
with tqdm(total=total_genomes, desc="Downloading assemblies", unit="genome") as pbar:
    for idx, row in df.iterrows():
        accession = row['assembly_accession']
        taxon = row['taxon']

        taxon_dir = OUTPUT_DIR / taxon
        taxon_dir.mkdir(exist_ok=True)

        temp_unpack_dir = taxon_dir / f"{accession}_temp"
        temp_unpack_dir.mkdir(exist_ok=True)

        zip_path = taxon_dir / f"{accession}.zip"

        cmd = ["datasets", "download", "genome", "accession", accession, "--filename", str(zip_path)]
        subprocess.run(cmd, check=True)

        unzip_file(zip_path, temp_unpack_dir)

        assembly_level = get_assembly_level_from_jsonl(temp_unpack_dir)

        final_folder = taxon_dir / f"{accession}_{assembly_level}"
        temp_unpack_dir.rename(final_folder)

        rename_fna_files(final_folder, accession, assembly_level)

        zip_path.unlink(missing_ok=True)

        pbar.update(1)

print("\nCompleted. All assemblies downloaded, unzipped, renamed (using assemblyLevel), and ZIP files deleted successfully.")
