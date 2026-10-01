# Kruskall_and_Dunn's.R

## Function

Performs the overall test and Dunn comparisons with Benjamini–Hochberg correction; exports the pairwise table to CSV.

## Overview

Compare experimental groups using Kruskal–Wallis and pairwise Dunn tests.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Requires readxl, dunn.test and FSA; the script includes package installation. Set file_path and sheet_name to an Excel sheet with Number and N_Rate columns. Run in RStudio or `source("Kruskall_and_Dunn's.R", echo = TRUE)`. Writes DunnTest_Results.csv.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
