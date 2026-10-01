# ANOVA_and_Tukey_HSD_with_Results_Export.R

## Function

Filters groups 1–7, runs ANOVA and Tukey HSD, and adds the studentised-range q statistic and residual degrees of freedom to the exported comparisons.

## Overview

Export a detailed table of pairwise group comparisons following ANOVA.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr, tidyr, tibble and writexl. Set the input Excel path and sheet; provide Number and numeric N_Rate. Run in RStudio or `source("ANOVA_and_Tukey_HSD_with_Results_Export.R", echo = TRUE)`. Writes tukey_results_with_stats.xlsx.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
