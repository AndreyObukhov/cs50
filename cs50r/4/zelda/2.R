library("tidyverse")
load("zelda.RData")
zelda <- zelda |>
  group_by(year) |>
  summarise(releases = n()) |>
  arrange(desc(releases))

save(zelda, file = "2.RData")