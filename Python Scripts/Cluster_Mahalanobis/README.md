# Cluster_Mahalanobis.py

## Function

Combines candidate CSV files, removes incomplete/non-finite numeric rows and constant features, calculates regularised Mahalanobis distances, and averages distances by cluster.

## Overview

Rank protein clusters by how closely their numerical features resemble the overall candidate dataset.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install pandas, numpy and scipy. Set root_dir to a folder containing *_FilteredCandidates_WET.csv files and clusters.faa.clstr. CSV files need an ID column matching sequence IDs in the cluster file and at least two varying numeric features. Run `python Cluster_Mahalanobis.py`. Writes GLOBAL_CLUSTER_MAHALANOBIS.csv.

Folder paths are placeholders: Input_Folder. Replace them with your own locations before running. Relative paths are resolved from the working directory.
