bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")
services <- rbind(bus, rail)
input <- readline("Route: ")
scope <- subset(services, route == input)
peak <- mean(scope[scope$peak == "PEAK", ]$numerator / scope[scope$peak == "PEAK", ]$denominator)
off_peak <- mean(scope[scope$peak == "OFF_PEAK", ]$numerator / scope[scope$peak == "OFF_PEAK", ]$denominator)
peak <- round(peak, 2) * 100
off_peak <- round(off_peak, 2) * 100
cat("On time ",peak,"% of the time during peak hours.\n", sep ="")
cat("On time ",off_peak,"% of the time during off-peak hours.\n", sep ="")