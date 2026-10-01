library(readxl)
library(dplyr)
library(purrr)
library(broom)
library(writexl)

file_path <- "Input_Folder/Input_Data.xlsx"
sheet_name <- "Sheet1"

data <- read_excel(file_path, sheet = sheet_name)

if (!all(c("Number", "N_Rate") %in% colnames(data))) {
  stop("Required columns 'Number' and 'N_Rate' not found in the dataset.")
}

groups <- unique(data$Number)
group_pairs <- combn(groups, 2, simplify = FALSE)

t_test_results <- map_df(group_pairs, function(pair) {
  group1 <- data %>% filter(Number == pair[1]) %>% pull(N_Rate)
  group2 <- data %>% filter(Number == pair[2]) %>% pull(N_Rate)

  t_test <- t.test(group1, group2)

  tidy(t_test) %>%
    mutate(group1 = pair[1],
           group2 = pair[2],
           Df = parameter) %>%
    select(-parameter)
})

output_file <- "t_test_results.xlsx"
write_xlsx(t_test_results, path = output_file)

message("T-test results have been saved to ", output_file)
