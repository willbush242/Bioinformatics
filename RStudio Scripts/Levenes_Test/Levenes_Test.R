install.packages(c("readxl", "car"))

library(readxl)
library(car)

file_path <- "Input_Folder/Input_Data.xlsx"
sheet_name <- "your_sheet_name"

data <- read_excel(file_path, sheet = sheet_name)

data$Number <- as.factor(data$Number)

levene_result <- leveneTest(N_Rate ~ Number, data = data)

print(levene_result)
