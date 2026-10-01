# Numbered_Barchart.R

## Function

Filters groups 1–7 and plots mean N_Rate with ± standard deviation error bars.

## Overview

Plot mean respiration rates for numbered experimental groups.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr and ggplot2. Set the Excel path and sheet; provide Number and N_Rate columns. Adjust the title and group selection if required. Run in RStudio or `source("Numbered_Barchart.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
