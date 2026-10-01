library(readxl)
library(dplyr)
library(ggplot2)

data <- read_excel("Input_Folder/Input_Data.xlsx", sheet = "Sheet1")

data_clean <- data %>%
  filter(!is.na(Number), !is.na(N_Rate)) %>%
  filter(Number %in% 1:7)

data_clean$Number <- factor(data_clean$Number)

summary_data <- data_clean %>%
  group_by(Number) %>%
  summarise(
    mean_value = mean(N_Rate, na.rm = TRUE),
    sd_value = sd(N_Rate, na.rm = TRUE)
  )

ggplot(summary_data, aes(x = Number, y = mean_value)) +
  geom_col(fill = "lightblue", color = "black") +
  geom_errorbar(aes(
    ymin = mean_value - sd_value,
    ymax = mean_value + sd_value
  ), width = 0.2, color = "black") +
  labs(
    title = "WH7803",
    x = "Stock",
    y = expression("Rate (" * mu * "mol O"[2] * " mg protein"^{-1} * " s"^{-1} * ")")
  ) +
  scale_y_continuous(
    breaks = seq(0, max(summary_data$mean_value + summary_data$sd_value, na.rm = TRUE) + 20, by = 20)
  ) +
  theme_minimal() +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    axis.line = element_line(color = "black", linewidth = 0.8),
    panel.border = element_blank(),
    axis.text.x = element_text(angle = 0, hjust = 0.5)
  )
