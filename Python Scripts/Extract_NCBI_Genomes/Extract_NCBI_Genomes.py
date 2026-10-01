from Bio import Entrez
import csv
import time
from tqdm import tqdm

Entrez.email = "your.email@example.com"

TAXA = [
    "Chlorophyta",
    "Mesostigmatophyceae",
    "Chlorokybophyceae",
    "Klebsormidiophyceae",
    "Charophyceae",
    "Zygnematophyceae",
    "Coleochaetophyceae"
]

OUTPUT_CSV = "genbank_assemblies_by_taxon.csv"

def get_assembly_ids_for_taxon(taxon, retmax=10000):
    term = f"{taxon}[Organism]"
    handle = Entrez.esearch(db="assembly", term=term, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def get_assembly_summary(assembly_uid):
    handle = Entrez.esummary(db="assembly", id=assembly_uid, report="full")
    rec = Entrez.read(handle)
    handle.close()
    return rec

all_rows = []

for tax in TAXA:
    print(f"\nProcessing taxon: {tax}")
    uids = get_assembly_ids_for_taxon(tax)
    if not uids:
        print(f" → No assemblies found for {tax}")
        continue

    print(f" → Found {len(uids)} assembly UIDs for {tax}")

    for uid in tqdm(uids, desc=f"{tax} genomes", unit="genome"):
        try:
            summary = get_assembly_summary(uid)
        except Exception as e:
            print(f"  ! Error fetching summary for UID {uid}: {e}")
            continue

        docsum = summary["DocumentSummarySet"]["DocumentSummary"][0]

        syn = docsum.get("Synonym", {})
        genbank_acc = syn.get("Genbank")
        if isinstance(genbank_acc, list):
            gb_accs = genbank_acc
        elif isinstance(genbank_acc, str):
            gb_accs = [genbank_acc]
        else:
            gb_accs = []

        if not gb_accs:
            continue

        row = {
            "taxon": tax,
            "assembly_uid": uid,
            "assembly_accession": docsum.get("AssemblyAccession"),
            "assembly_name": docsum.get("AssemblyName"),
            "genbank_accessions": ";".join(gb_accs),
            "biology_category": docsum.get("AssemblyType"),
            "submitter": docsum.get("SubmitterOrganization"),
            "biosample": docsum.get("BioSampleAccn"),
            "bioproject": docsum.get("BioprojectAccn"),
            "version": docsum.get("VersionStatus")
        }
        all_rows.append(row)

        time.sleep(0.34)

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "taxon",
        "assembly_uid",
        "assembly_accession",
        "assembly_name",
        "genbank_accessions",
        "biology_category",
        "submitter",
        "biosample",
        "bioproject",
        "version"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in all_rows:
        writer.writerow(r)

print(f"\nCompleted. Wrote {len(all_rows)} GenBank assemblies to {OUTPUT_CSV}")
