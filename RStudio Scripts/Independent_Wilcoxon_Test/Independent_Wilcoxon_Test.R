library(readxl)
library(dplyr)
library(purrr)
library(broom)
library(writexl)

file_path <- "Input_Folder/Input_Data.xlsx"
sheet_name <- "Sheet1"
output_file <- "wilcoxon_results.xlsx"

data <- read_excel(file_path, sheet = sheet_name)

if (!all(c("Number", "N_Rate") %in% colnames(data))) {
  stop("Error: Required columns 'Number' and 'N_Rate' are missing.")
}

groups <- unique(data$Number)
group_pairs <- combn(groups, 2, simplify = FALSE)

wilcoxon_results <- map_df(group_pairs, function(pair) {
  group1 <- data %>% filter(Number == pair[1]) %>% pull(N_Rate)
  group2 <- data %>% filter(Number == pair[2]) %>% pull(N_Rate)

  test <- wilcox.test(group1, group2, exact = FALSE)

  tidy(test) %>%
    mutate(group1 = pair[1],
           group2 = pair[2]) %>%
    select(group1, group2, statistic, p.value, method, alternative)
})

write_xlsx(wilcoxon_results, output_file)

cat("Wilcoxon test results saved to:", output_file, "\n")
