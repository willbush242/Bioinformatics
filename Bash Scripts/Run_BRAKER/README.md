# Run_BRAKER.sh

## Function

Loops over *.fasta files, provides a reference protein set, reuses the AUGUSTUS species configuration chlamy and assigns a separate working directory to each genome; uses eight threads.

## Overview

Run BRAKER gene prediction across a folder of genome FASTA files.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Run in Ubuntu on Windows Subsystem for Linux (WSL), with BRAKER and its dependencies configured. Set GENOME_DIR, OUTDIR, TEMPLATE (protein FASTA) and BRAKER (braker.pl executable). Use Linux paths, for example /mnt/d/Input_Genomes for D:\Input_Genomes. Ensure the chlamy species configuration exists or change --species. Run `bash Run_BRAKER.sh`.

Folder paths are placeholders: /mnt/d/Input_Genomes, /mnt/d/Output_BRAKER, /mnt/d/Input_Proteins/reference_proteins.faa. Replace them with your own locations before running. Relative paths are resolved from the working directory.
