y2020 <- read.csv("2020.csv")
y2021 <- read.csv("2021.csv")
y2022 <- read.csv("2022.csv")
y2023 <- read.csv("2023.csv")
y2024 <- read.csv("2024.csv")

y2020$year <- 2020
y2021$year <- 2021
y2022$year <- 2022
y2023$year <- 2023
y2024$year <- 2024

data <- rbind(y2020, y2021, y2022, y2023, y2024)

country_name <- readline("Country: ")
data1 <- subset(data, data$country == country_name)
for (i in 2020:2024) {
  if (i %in% data1$year) {
    data2 <- subset(data1, data1$year == i)
    happiness <- round(sum(data2[2:(length(data2)-1)]), digits = 2)
    cat(paste0(country_name, " (",i,"): ", happiness), "\n")
  } else {
    cat(paste0(country_name, " (",i,"): data unavailable\n"))
  }
}