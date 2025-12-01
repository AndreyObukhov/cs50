calculate_growth_rate <- function(years, visitors) {
  growth_rate <- (visitors[length(visitors)] - visitors[1]) /
    (years[length(years)] - years[1])
}


predict_visitors <- function(years, visitors, year) {
  growth_rate <- calculate_growth_rate(years, visitors)
  year <- year - years[1] + 1
  if (year <= length(years)) {
    return(visitors[year])
  } else {
    prediction <- visitors[length(visitors)] +
      (growth_rate * (year - length(years)))
    return(prediction)
  }
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
