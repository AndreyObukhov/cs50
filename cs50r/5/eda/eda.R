library("tidyverse")
editors <- read_csv("active_editors.csv")
editors <- editors |>
  select(
    month,
    active_editors = total.total,
  )

p1 <- ggplot(editors, aes(x=month, y=active_editors)) +
  geom_line(color="#69b3a2", linewidth = 1) +
  ggtitle("Active editors in English Wikipedia") +
  labs(x = NULL, y = "Active editors") +
  theme_classic()

ggsave(
  "visualization.png",
  plot = p1,
  width = 1200,
  height = 900,
  units = "px"
)