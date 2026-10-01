# R analysis and plotting scripts

## Function

Analyse experimental measurements using statistical tests, compare groups, export results and produce plots with summary statistics and error bars.

## Overview

R scripts for analysing and visualising biological research data in RStudio. The collection includes distribution and variance checks, parametric and non-parametric group comparisons, and bar charts and box plots.

## Contents

ANOVA_and_Tukey_HSD_with_Results_Export - Export a detailed table of pairwise group comparisons following ANOVA.

ANOVA_Tukey_HSD - Compare group means using one-way ANOVA and Tukey comparisons.

Box_Plot_Script - Display the distribution of normalised oxygen-consumption measurements by group.

Independent_Welch_T-Test - Calculate pairwise comparisons of respiration measurements between groups.

Independent_Wilcoxon_Test - Compare respiration measurements between every pair of experimental groups.

Kruskal_Wallis_Test - Compare respiration measurements across experimental groups using a Kruskal–Wallis test.

Kruskall_and_Dunn's - Compare experimental groups using Kruskal–Wallis and pairwise Dunn tests.

Levenes_Test - Assess equality of variance between experimental groups.

Mean_Bar_Chart_with_SD_error_bars - Compare respiration measurements across six conditions belonging to two strains.

Named_Barchart - Plot mean respiration rates for named experimental groups.

Numbered_Barchart - Plot mean respiration rates for numbered experimental groups.

Shapiro_Wilk_Test - Assess the distribution of respiration measurements within each experimental group.

## Context and contribution

The scripts currently collected here were developed for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Open the relevant folder and follow its README. Install the listed R packages, update file paths and sheet names, and check that the input columns match those expected by the script. Run the script in RStudio or with source(). Some scripts expect an existing data frame in the R session. Choose tests appropriate to the experimental design; the pairwise Welch and Wilcoxon scripts export unadjusted p-values.
