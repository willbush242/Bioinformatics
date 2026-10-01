# Run_Braker_Skip_Optimise.sh

## Function

Loops over *.fasta files, derives each species name from the filename and uses --esmode, --skipOptimize and eight threads, with a separate output directory per genome.

## Overview

Batch-run BRAKER in ES mode without parameter optimisation.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Run in Ubuntu on WSL with BRAKER and its dependencies configured. Set GENOME_DIR, OUTDIR and BRAKER using Linux paths; a Windows D: drive is normally /mnt/d. Run `bash Run_Braker_Skip_Optimise.sh`.

Folder paths are placeholders: /mnt/d/Input_Genomes, /mnt/d/Output_BRAKER. Replace them with your own locations before running. Relative paths are resolved from the working directory.
