library(ggplot2)
library(dplyr)

ggplot(data, aes(x = factor(Group), y = N1_2secR)) +

  geom_boxplot(fill = "skyblue", color = "black") +

  stat_summary(
    fun.data = function(x) {
      m  <- mean(x)
      sd <- sd(x)
      data.frame(y = m, ymin = m - sd, ymax = m + sd)
    },
    geom  = "errorbar",
    width = 0.2,
    color = "black"
  ) +
  stat_summary(fun = mean, geom = "point", size = 2, color = "black") +

  labs(
    title = "Distribution of N1_2secR by Stock",
    x     = "Stock",
    y     = expression(mu*"mol O"[2]~"mg protein"^{-1}~s^{-1})
  ) +

  theme(
    panel.background   = element_blank(),
    panel.grid.major   = element_blank(),
    panel.grid.minor   = element_blank(),
    axis.line          = element_line(color = "black"),
    axis.title         = element_text(size = 12),
    axis.text          = element_text(size = 10)
  )
