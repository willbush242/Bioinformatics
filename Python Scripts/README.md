# Python research scripts

## Function

Automate genome-data retrieval, organise assembly metadata, summarise and filter genome-completeness results, rank protein clusters, and prepare presence/absence annotations for iTOL.

## Overview

Python scripts from my third- and fourth-year university research projects. These tools support different stages of data preparation and analysis, with inputs and outputs described in each script folder.

## Contents

Cluster_Mahalanobis - Rank protein clusters by how closely their numerical features resemble the overall candidate dataset.

convert_presence_absence_to_itol - Convert a presence/absence spreadsheet into an iTOL annotation file.

Create_BUSCO_Output_Excel - Collect genome completeness summaries into one Excel workbook.

Extract_Assembly_Metadata - Gather downloaded assembly metadata into one directory.

Extract_Filtered_BUSCO_List - Select assembly accessions meeting defined genome-completeness thresholds.

Extract_Genomes_from_NCBI_Datasets - Download genome assemblies listed in a research metadata table.

Extract_NCBI_Genomes - Build a table of NCBI genome assemblies for selected green-algal groups.

Retrieve_taxonomic_lineages - Retrieve taxonomic lineages for a selected list of genome assemblies.

## Context and contribution

I developed these scripts for research into respiration in marine microorganisms and carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Open the relevant folder and read its README for dependencies, expected input columns and configuration. Install the required Python packages, replace placeholder paths and run the selected script with Python. NCBI retrieval tools require an internet connection; the genome downloader also requires the NCBI datasets command. Review project-specific thresholds and settings before using new data.
