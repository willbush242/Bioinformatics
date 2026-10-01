# Levenes_Test.R

## Function

Reads Excel, converts Number to a factor and runs the car package’s Levene test with its default median centre.

## Overview

Assess equality of variance between experimental groups.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Requires readxl and car; the script includes package installation. Set file_path and sheet_name. Supply Number and numeric N_Rate columns. Run in RStudio or `source("Levenes_Test.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
