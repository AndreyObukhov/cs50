library("tidyverse")
load("air.RData")
air <- air |>
  filter(county == "OR - Crook")
save(air, file = "3.RData")