# Extract_Assembly_Metadata.py

## Function

Traverses taxon folders and GCA_ assembly folders, copying each assembly_data_report.jsonl to a filename based on its assembly folder.

## Overview

Gather downloaded assembly metadata into one directory.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Uses the Python standard library. Set BASE_DIR to the download root and METADATA_DIR to the destination. Expected layout: BASE_DIR/taxon/GCA_.../ncbi_dataset/data/assembly_data_report.jsonl. Run `python Extract_Assembly_Metadata.py`.

Folder paths are placeholders: Input_Genomes, Output_Metadata. Replace them with your own locations before running. Relative paths are resolved from the working directory.
Set Input_Genomes to the genome-download directory (Output_Genomes if using the download script with its default folder name).
