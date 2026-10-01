# convert_presence_absence_to_itol.py

## Function

Transposes a matrix from clusters-by-strains to strains-by-clusters and writes labels, cycling colours, shape fields and values in DATASET_BINARY format.

## Overview

Convert a presence/absence spreadsheet into an iTOL annotation file.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and  debugged issues.

## How to use

This is a Python script, despite its RStudio folder. Install pandas and openpyxl. Provide Input_Folder/Input_Presence_Absence.xlsx with Sheet1, cluster labels in the first column and strain names as remaining column headings. Run `python "convert_presence_absence_to_itol.py"`. Writes itol_dataset_binary.txt for use with matching tree-tip names.

Folder paths are placeholders: Input_Folder/Input_Presence_Absence.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
