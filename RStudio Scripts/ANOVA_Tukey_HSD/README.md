# ANOVA_Tukey_HSD.R

## Function

Reads Excel, removes missing group/measurement rows, retains Number groups 1–7 and runs ANOVA followed by TukeyHSD.

## Overview

Compare group means using one-way ANOVA and Tukey comparisons.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr and ggplot2. Set the input path and sheet; supply Number and numeric N_Rate columns. Run in RStudio or `source("ANOVA_Tukey_HSD.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
