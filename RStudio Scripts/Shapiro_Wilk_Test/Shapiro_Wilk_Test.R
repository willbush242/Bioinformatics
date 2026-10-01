install.packages(c("readxl", "writexl"))

library(readxl)
library(writexl)

file_path <- "Input_Folder/Input_Data.xlsx"
sheet_name <- "your_sheet_name"
data <- read_excel(file_path, sheet = sheet_name)

data$Number <- as.factor(data$Number)

shapiro_list <- by(data$N_Rate, data$Number, shapiro.test)

shapiro_df <- do.call(rbind, lapply(names(shapiro_list), function(group) {
  test <- shapiro_list[[group]]
  data.frame(
    Group = group,
    W = test$statistic,
    p_value = test$p.value
  )
}))

write_xlsx(shapiro_df, "Shapiro_Wilk_Results.xlsx")
