library(readxl)
library(dplyr)
library(ggplot2)

data <- read_excel("Input_Folder/Input_Data.xlsx", sheet = "Sheet1")

data_clean <- data %>%
  filter(!is.na(Number), !is.na(N_Rate)) %>%
  filter(Number %in% 1:6)

data_clean$Number <- factor(data_clean$Number)

summary_data <- data_clean %>%
  group_by(Number) %>%
  summarise(
    mean_value = mean(N_Rate, na.rm = TRUE),
    sd_value = sd(N_Rate, na.rm = TRUE)
  ) %>%
  ungroup()

color_pattern <- c("red", "orange", "red", "orange", "red", "orange")
group_labels <- c("WH7803", "WH8102")

summary_data <- summary_data %>%
  mutate(
    color = color_pattern[as.numeric(as.character(Number))],
    group = factor(color, levels = c("red", "orange"), labels = group_labels)
  )

ggplot(summary_data, aes(x = Number, y = mean_value, fill = group)) +
  geom_col(color = "black") +
  geom_errorbar(aes(
    ymin = mean_value - sd_value,
    ymax = mean_value + sd_value
  ), width = 0.2, color = "black") +
  scale_fill_manual(values = c("WH7803" = "red", "WH8102" = "orange")) +
  labs(
    title = "WH7803 and WH8102",
    x = "Stock",
    y = expression("Rate (" * mu * "mol O"[2] * " mg protein"^{-1} * " s"^{-1} * ")"),
    fill = "Group"
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
