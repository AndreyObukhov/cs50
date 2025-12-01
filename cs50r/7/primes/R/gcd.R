gcd <- function(a = 1, b = 1) {
  while (b != 0) {
    temp <- b
    b <- a %% b
    a <- temp
  }
  return(abs(a))
}