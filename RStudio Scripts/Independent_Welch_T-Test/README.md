# Independent_Welch_T-Test.R

## Function

Checks required columns, runs independent Welch t-tests for all group pairs and exports estimates, test statistics, degrees of freedom and unadjusted p-values.

## Overview

Calculate pairwise comparisons of respiration measurements between groups.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr, purrr, broom and writexl. Set file_path, sheet_name and output_file; provide Number and numeric N_Rate columns with at least two groups. Run in RStudio or `source("Independent_Welch_T-Test.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
