# Named_Barchart.R

## Function

Groups by Stock and draws mean bars with ± standard deviation error bars and rotated group labels.

## Overview

Plot mean respiration rates for named experimental groups.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl, dplyr and ggplot2. Set the Excel path and sheet; provide Stock and numeric N_Rate columns. Adjust the chart title for the dataset. Run in RStudio or `source("Named_Barchart.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
