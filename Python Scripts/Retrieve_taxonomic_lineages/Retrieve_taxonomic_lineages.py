import pandas as pd
from Bio import Entrez
from tqdm import tqdm

Entrez.email = "your.email@example.com"

TXT_FILE = r"GCA_names_filtered.txt"
OUTPUT_FILE = r"assembly_taxonomy.xlsx"

def get_lineage_from_accession(accession):
    try:
        handle = Entrez.esearch(db="assembly", term=accession)
        record = Entrez.read(handle)
        handle.close()

        if len(record["IdList"]) == 0:
            return None

        asm_id = record["IdList"][0]

        handle = Entrez.esummary(db="assembly", id=asm_id, report="full")
        summary = Entrez.read(handle)
        handle.close()

        taxid = summary['DocumentSummarySet']['DocumentSummary'][0].get("Taxid")
        if not taxid:
            return None

        handle = Entrez.efetch(db="taxonomy", id=taxid, retmode="xml")
        taxdata = Entrez.read(handle)[0]
        handle.close()

        ranks = {d["Rank"]: d["ScientificName"] for d in taxdata["LineageEx"]}
        ranks["species"] = taxdata.get("ScientificName", "")
        return ranks

    except Exception as e:
        print(f"Error retrieving taxonomy for {accession}: {e}")
        return None

def assign_chlorophyte_group(ranks):
    class_name = ranks.get("class", "")

    prasinophyte_classes = {
        "Prasinophyceae",
        "Mamiellophyceae",
        "Pyramimonadophyceae",
        "Nephrophyceae"
    }

    core_chlorophyte_classes = {
        "Chlorophyceae",
        "Trebouxiophyceae",
        "Ulvophyceae"
    }

    if class_name in prasinophyte_classes:
        return "Prasinophyte"

    if class_name in core_chlorophyte_classes:
        return "Core Chlorophyte"

    if "Streptophyta" in ranks.values():
        return "Streptophyte"

    return "Other"

with open(TXT_FILE, 'r') as f:
    accessions = [line.strip() for line in f if line.strip()]

records = []

for acc in tqdm(accessions, desc="Retrieving phylogeny", unit="assembly"):
    ranks = get_lineage_from_accession(acc)

    if ranks is None:
        records.append({"accession": acc, "status": "Not found"})
        continue

    group = assign_chlorophyte_group(ranks)

    row = {"accession": acc, "group": group}
    row.update(ranks)
    records.append(row)

out_df = pd.DataFrame(records)
out_df.to_excel(OUTPUT_FILE, index=False)

print("\nCompleted. Saved phylogeny to:")
print(OUTPUT_FILE)
