# [Me] Code function in R to detect all prime numbers in the input vector.

# [ChatGPT] You can create a function in R to identify all
# prime numbers in an input vector using the following code:
is_prime <- function(n) {
  if (n <= 1) {
    return(FALSE)
  }
  for (i in 2:sqrt(n)) {
    if (n %% i == 0) {
      return(FALSE)
    }
  }
  return(TRUE)
}

believe <- function(vec) {
  primes <- vec[sapply(vec, is_prime)]
  return(primes)
}
