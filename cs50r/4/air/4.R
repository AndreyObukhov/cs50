library("tidyverse")
load("air.RData")
air <- air |>
  filter(county == "OR - Crook") |>
  arrange(desc(emissions))
save(air, file = "4.RData")