library("tidyverse")
load("air.RData")
air <- air |>
  select(source = level_1, pollutant, emissions) |>
  group_by(source, pollutant) |>
  summarise(emissions = sum(emissions))
save(air, file = "7.RData")