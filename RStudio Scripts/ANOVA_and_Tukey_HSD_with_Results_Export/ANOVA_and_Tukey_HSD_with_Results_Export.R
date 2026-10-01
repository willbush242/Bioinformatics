library(readxl)
library(dplyr)
library(tidyr)
library(tibble)

data <- read_excel("Input_Folder/Input_Data.xlsx", sheet = "Sheet1")

data_clean <- data %>%
  filter(!is.na(Number), !is.na(N_Rate)) %>%
  filter(Number %in% 1:7)

data_clean$Number <- factor(data_clean$Number)

anova_result <- aov(N_Rate ~ Number, data = data_clean)
summary(anova_result)

tukey_result <- TukeyHSD(anova_result)

tk_df <- as.data.frame(tukey_result$Number) %>%
  rownames_to_column("comparison") %>%
  separate(comparison, into = c("g1", "g2"), sep = "-")

df_res <- df.residual(anova_result)
mse <- summary(anova_result)[[1]]["Residuals", "Mean Sq"]

group_sizes <- table(data_clean$Number)

tk_df <- tk_df %>%
  rowwise() %>%
  mutate(
    se = sqrt(mse / 2 * (1 / group_sizes[g1] + 1 / group_sizes[g2])),
    q = abs(diff) / se,
    df = df_res
  ) %>%
  ungroup() %>%
  select(g1, g2, diff, lwr, upr, q, df, `p adj`)

print(tk_df)

library(writexl)
write_xlsx(tk_df, "tukey_results_with_stats.xlsx")
