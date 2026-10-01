# Extract_NCBI_Genomes.py

## Function

Searches the assembly database by taxon and collects assembly identifiers, names, accessions and related metadata into CSV.

## Overview

Build a table of NCBI genome assemblies for selected green-algal groups.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install biopython and tqdm. Set Entrez.email to your own contact email locally, edit TAXA if needed, and choose OUTPUT_CSV. With an internet connection, run `python Extract_NCBI_Genomes.py`. The resulting CSV supplies assembly_accession and taxon fields used by the download script.
