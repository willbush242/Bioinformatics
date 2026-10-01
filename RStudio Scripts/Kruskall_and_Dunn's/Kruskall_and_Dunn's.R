install.packages(c("readxl", "dunn.test", "FSA"))

library(readxl)
library(dunn.test)
library(FSA)

file_path <- "Input_Folder/Input_Data.xlsx"
sheet_name <- "Sheet_1"

data <- read_excel(file_path, sheet = sheet_name)

kruskal_result <- kruskal.test(N_Rate ~ as.factor(Number), data = data)
print(kruskal_result)

dunn_result <- dunnTest(N_Rate ~ as.factor(Number), data = data, method = "bh")

print(dunn_result)

write.csv(dunn_result$res, "DunnTest_Results.csv", row.names = FALSE)
