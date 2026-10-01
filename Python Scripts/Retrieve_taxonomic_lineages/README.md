# Retrieve_taxonomic_lineages.py

## Function

Looks up assembly taxon IDs, retrieves lineage ranks and labels records as Prasinophyte, Core Chlorophyte, Streptophyte or Other. This retrieves taxonomy; it does not infer a phylogenetic tree.

## Overview

Retrieve taxonomic lineages for a selected list of genome assemblies.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install pandas, biopython, tqdm and openpyxl. Set Entrez.email locally, TXT_FILE to a list of assembly accessions (one per line), and OUTPUT_FILE to an .xlsx file. With an internet connection, run `python Retrieve_taxonomic_lineages.py`.
