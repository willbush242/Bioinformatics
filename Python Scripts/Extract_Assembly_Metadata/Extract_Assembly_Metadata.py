from pathlib import Path
import shutil

BASE_DIR = Path(r"Input_Genomes")
METADATA_DIR = Path(r"Output_Metadata")

METADATA_DIR.mkdir(parents=True, exist_ok=True)

for class_folder in BASE_DIR.iterdir():
    if class_folder.is_dir():

        for gca_folder in class_folder.iterdir():
            if gca_folder.is_dir() and gca_folder.name.startswith("GCA_"):

                jsonl_path = gca_folder / "ncbi_dataset" / "data" / "assembly_data_report.jsonl"
                if jsonl_path.exists():

                    new_name = f"{gca_folder.name}.jsonl"
                    destination = METADATA_DIR / new_name
                    shutil.copy2(jsonl_path, destination)
                    print(f"Copied: {jsonl_path} → {destination}")
                else:
                    print(f"Missing JSONL: {jsonl_path}")
