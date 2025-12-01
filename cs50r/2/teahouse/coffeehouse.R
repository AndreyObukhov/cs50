size <- readline("Size: ")
milk <- readline("Milk: ")
if (size == "Small" & milk == "Yes") {
  cat("You might like cappuccino ☕", "\n")
}
if (size == "Small" & milk == "No") {
  cat("You might like espresso ☕", "\n")
}
if (size == "Big" & milk == "Yes") {
  cat("You might like latte ☕", "\n")
}
if (size == "Big" & milk == "No") {
  cat("You might like americano ☕", "\n")
}
if (size != "Small" & size != "Big") {
  cat("Enter either 'Small' or 'Big' for size", "\n")
}
if (milk != "Yes" & milk != "No") {
  cat("Enter either 'No' or 'Yes' for milk", "\n")
}
