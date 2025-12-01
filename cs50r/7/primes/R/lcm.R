# Function to calculate the LCM of two numbers
lcm <- function(a = 1, b = 1) {
  if (a == 0 | b == 0) {
    return(0)  # LCM is not defined for zero
  }
  return(abs(a * b) / gcd(a, b))
}

# Example usage
lcm(12, 15)  # Should return 60