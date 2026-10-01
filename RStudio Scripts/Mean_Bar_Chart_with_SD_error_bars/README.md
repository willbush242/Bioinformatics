# Mean_Bar_Chart_with_SD_error_bars.R

## Function

Plots means with ± standard deviation error bars, alternating colours and a two-strain legend.

## Overview

Compare respiration measurements across six conditions belonging to two strains.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr and ggplot2. Set the Excel path and sheet; provide Number (1–6) and N_Rate. Edit group_labels, scale_fill_manual and the title together if changing strain names. Odd group numbers map to the first strain and even numbers to the second. Run in RStudio or `source("Mean_Bar_Chart_with_SD_error_bars.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
