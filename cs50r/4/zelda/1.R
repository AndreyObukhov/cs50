library("tidyverse")
zelda <- read_csv("zelda.csv")
zelda$year <- zelda$release |>
  word(1, sep = fixed(" - "))
zelda$system <- zelda$release |>
  word(2, sep = fixed(" - "))
zelda <- zelda |>
  select(title, year, system, role, names)

zelda <- pivot_wider(
  zelda,
  id_cols = c(title, year, system),
  names_from = role,
  values_from = names
)

zelda <- zelda |>
  rename_with(tolower)

save(zelda, file = "zelda.RData")