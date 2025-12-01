library("tidyverse")
load("air.RData")
air <- air |>
  select(pollutant, emissions) |>
  group_by(pollutant) |>
  summarize(emissions = sum(emissions)) |>
  arrange(desc(emissions))
save(air, file = "6.RData")