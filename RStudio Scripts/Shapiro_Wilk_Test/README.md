# Shapiro_Wilk_Test.R

## Function

Runs Shapiro–Wilk tests by Number and exports each group’s W statistic and p-value to Excel.

## Overview

Assess the distribution of respiration measurements within each experimental group.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Requires readxl and writexl; the script includes package installation. Set file_path and sheet_name and provide Number and numeric N_Rate columns. Each group needs 3–5000 non-missing observations and non-identical values. Run in RStudio or `source("Shapiro_Wilk_Test.R", echo = TRUE)`. Writes Shapiro_Wilk_Results.xlsx.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
