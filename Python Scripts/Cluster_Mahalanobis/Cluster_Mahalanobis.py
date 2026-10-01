import os
import pandas as pd
import numpy as np
from scipy.spatial.distance import mahalanobis

root_dir = r"Input_Folder"

all_dfs = []

for dirpath, _, filenames in os.walk(root_dir):

    for file in filenames:

        if file.endswith("_FilteredCandidates_WET.csv"):

            file_path = os.path.join(dirpath, file)

            try:
                df = pd.read_csv(file_path)
                df["Source_File"] = file_path
                all_dfs.append(df)

            except Exception as e:
                print(f"FAILED to read {file_path} -> {e}")

if len(all_dfs) == 0:
    raise RuntimeError("No valid files found.")

df = pd.concat(all_dfs, ignore_index=True)

print("GLOBAL SHAPE:", df.shape)

df["ID"] = (
    df["ID"]
    .astype(str)
    .str.replace(">", "", regex=False)
    .str.strip()
)

X = df.select_dtypes(include=[np.number]).copy()

X = X.apply(pd.to_numeric, errors="coerce")
X = X.replace([np.inf, -np.inf], np.nan)

mask = X.notnull().all(axis=1)

X = X[mask]
df = df[mask].reset_index(drop=True)

print("After cleaning:", X.shape)

X = X.loc[:, X.std() > 0]

if X.shape[1] < 2:
    raise RuntimeError("Not enough numeric features.")

mu = X.mean().values
cov = np.cov(X.values, rowvar=False)
cov += np.eye(cov.shape[0]) * 1e-10
inv_cov = np.linalg.pinv(cov)

df["Mahalanobis_Distance"] = [
    mahalanobis(x, mu, inv_cov)
    for x in X.values
]

clstr_path = os.path.join(root_dir, "clusters.faa.clstr")

cluster_map = {}

current_cluster = None

with open(clstr_path) as f:

    for line in f:

        line = line.strip()

        if line.startswith(">Cluster"):

            current_cluster = int(
                line.replace(">Cluster", "").strip()
            )

        elif line and not line.startswith(">"):

            parts = line.split()

            seq = parts[2]
            seq = seq.replace(">", "")
            seq = seq.split("...")[0]
            seq = seq.strip()

            if seq not in cluster_map:
                cluster_map[seq] = []

            cluster_map[seq].append(current_cluster)

df["Cluster_IDs"] = df["ID"].map(cluster_map)

mapped_df = df.dropna(subset=["Cluster_IDs"]).copy()

mapped_df = mapped_df.explode("Cluster_IDs")

mapped_df["Cluster_IDs"] = mapped_df["Cluster_IDs"].astype(int)

print("\nMapped rows:", len(mapped_df))

cluster_scores = (
    mapped_df
    .groupby("Cluster_IDs")["Mahalanobis_Distance"]
    .mean()
    .reset_index()
)

cluster_scores.columns = [
    "Cluster_ID",
    "Cluster_Mahalanobis"
]

cluster_scores = cluster_scores.sort_values(
    "Cluster_Mahalanobis"
)

out_path = os.path.join(
    root_dir,
    "GLOBAL_CLUSTER_MAHALANOBIS.csv"
)

cluster_scores.to_csv(out_path, index=False)

print("\nDONE")

print("\nTotal clusters scored:")
print(len(cluster_scores))

print("\nTop most typical cluster:")
print(cluster_scores.iloc[0])

print("\nSaved to:")
print(out_path)

all_clusters = set(
    c for v in cluster_map.values() for c in v
)

scored_clusters = set(cluster_scores["Cluster_ID"])

print("\nExpected clusters:", len(all_clusters))
print("Scored clusters:", len(scored_clusters))
print("Missing:", len(all_clusters - scored_clusters))
