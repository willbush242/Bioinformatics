library(readxl)
library(dplyr)

data <- read_excel("Input_Folder/Input_Data.xlsx", sheet = "Sheet1")

data_clean <- data %>%
  filter(!is.na(Number), !is.na(N_Rate)) %>%
  filter(Number %in% 1:7)

data_clean$Number <- factor(data_clean$Number)

kruskal.test(N_Rate ~ Number, data = data_clean)
