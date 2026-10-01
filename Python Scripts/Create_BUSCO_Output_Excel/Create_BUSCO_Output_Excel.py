import os
import re
import pandas as pd
from tqdm import tqdm

folder_path = r"Input_BUSCO_Summaries"
output_excel = r"BUSCO_summary.xlsx"

rows = []

txt_files = []
for root, dirs, files in os.walk(folder_path):
    for f in files:
        if f.lower().endswith(".txt"):
            txt_files.append(os.path.join(root, f))

print(f"Found {len(txt_files)} BUSCO txt files.")

for file in tqdm(txt_files, desc="Processing BUSCO txt files"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read; skipping {file}: {e}")
        continue

    row = {}

    m_gca = re.search(r"Summarized benchmarking.*\/([^/]+)\.fna", content)
    row["GCA"] = m_gca.group(1) if m_gca else ""

    m_mode = re.search(r"BUSCO was run in mode: (\S+)", content)
    row["BUSCO_mode"] = m_mode.group(1) if m_mode else ""

    m_pred = re.search(r"Gene predictor used: (\S+)", content)
    row["Gene_predictor"] = m_pred.group(1) if m_pred else ""

    m_summary = re.search(r"C:(?P<C>[\d\.]+)%\[S:(?P<S>[\d\.]+)%,D:(?P<D>[\d\.]+)%\],F:(?P<F>[\d\.]+)%,M:(?P<M>[\d\.]+)%,n:(?P<n>\d+),E:(?P<E>[\d\.]+)%", content)
    if m_summary:
        row.update({k: float(v) if k not in ["n"] else int(v) for k,v in m_summary.groupdict().items()})
    else:
        row.update({"C":"","S":"","D":"","F":"","M":"","n":"","E":""})

    patterns = {
        "Complete_BUSCOs_C": r"(\d+)\s+Complete BUSCOs \(C\)\s+\(of which (\d+) contain internal stop codons\)",
        "Complete_S": r"(\d+)\s+Complete and single-copy BUSCOs \(S\)",
        "Complete_D": r"(\d+)\s+Complete and duplicated BUSCOs \(D\)",
        "Fragmented_F": r"(\d+)\s+Fragmented BUSCOs \(F\)",
        "Missing_M": r"(\d+)\s+Missing BUSCOs \(M\)",
        "Total_BUSCO_groups": r"(\d+)\s+Total BUSCO groups searched"
    }

    for key, pat in patterns.items():
        m = re.search(pat, content)
        if m:
            if key == "Complete_BUSCOs_C":
                row["Complete_BUSCOs_C"] = int(m.group(1))
                row["Internal_stop_codons"] = int(m.group(2))
            else:
                row[key] = int(m.group(1))
        else:
            row[key] = "" if key != "Complete_BUSCOs_C" else 0

    stats_patterns = {
        "Number_of_scaffolds": r"(\d+)\s+Number of scaffolds",
        "Number_of_contigs": r"(\d+)\s+Number of contigs",
        "Total_length": r"(\d+)\s+Total length",
        "Percent_gaps": r"([\d\.]+)%\s+Percent gaps",
        "Scaffold_N50_kbp": r"([\d]+)\s+kbp\s+Scaffold N50",
        "Contig_N50_kbp": r"([\d]+)\s+kbp\s+Contigs N50"
    }

    for key, pat in stats_patterns.items():
        m = re.search(pat, content)
        if m:
            row[key] = float(m.group(1)) if "." in m.group(1) else int(m.group(1))
        else:
            row[key] = ""

    dep_patterns = {
        "hmmsearch": r"hmmsearch:\s*(\S+)",
        "bbtools": r"bbtools:\s*(\S+)",
        "miniprot_index": r"miniprot_index:\s*(\S+)",
        "miniprot_align": r"miniprot_align:\s*(\S+)"
    }

    for key, pat in dep_patterns.items():
        m = re.search(pat, content)
        row[key] = m.group(1) if m else ""

    rows.append(row)

df = pd.DataFrame(rows)

df.to_excel(output_excel, index=False)
print(f"\nCompleted. Excel created: {output_excel}")
