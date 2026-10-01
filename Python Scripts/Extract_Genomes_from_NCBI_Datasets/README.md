# Extract_Genomes_from_NCBI_Datasets.py

## Function

Calls the NCBI datasets command, extracts downloaded archives, reads assembly-level metadata and organises downloads by taxon and assembly accession.

## Overview

Download genome assemblies listed in a research metadata table.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install pandas and tqdm, and make the NCBI datasets command available on PATH. Set CSV_FILE and OUTPUT_DIR. The CSV needs assembly_accession and taxon columns. Run `python Extract_Genomes_from_NCBI_Datasets.py`. Downloaded ZIP files are deleted after extraction. The script downloads every row supplied; select the desired assembly levels in the input table.

Folder paths are placeholders: Output_Genomes. Replace them with your own locations before running. Relative paths are resolved from the working directory.
