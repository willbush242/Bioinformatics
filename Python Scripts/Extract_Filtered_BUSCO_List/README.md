# Extract_Filtered_BUSCO_List.py

## Function

Filters BUSCO scores to C and S >= 95%, and D, F and M <= 2.5%, then exports the GCA identifiers.

## Overview

Select assembly accessions meeting defined genome-completeness thresholds.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install pandas and openpyxl. Set file_path to an Excel workbook containing GCA, C, S, D, F and M columns, with percentages stored on a 0–100 scale. Set output_file and run `python Extract_Filtered_BUSCO_List.py`. Writes one identifier per line.
