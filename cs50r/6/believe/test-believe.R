library(testthat)
source("believe.R")

test_that("`is_prime` works on its own", {
  expect_equal(is_prime(1), FALSE)
  expect_equal(is_prime(2), FALSE)
  expect_equal(is_prime(3), TRUE)
})

test_that("`find_primes` returns numeric(0) for input vector with no primes", {
  expect_equal(believe(c(1)), numeric(0))
  expect_equal(believe(c(1, 2)), numeric(0))
  expect_equal(believe(c(1, 2, 4, 8, 16)), numeric(0))
})

test_that("`find_primes` stops if input vector is not numeric", {
  expect_error(believe(c("a")))
  expect_error(believe(c("1", "2", "a")))
})

test_that("`find_primes` returns expected values for some examples", {
  expect_equal(believe(c(1, 7, 17)), c(7, 17))
  expect_equal(believe(c(37, 2, 101)), c(37, 101))
  expect_equal(believe(c(113, 128, 1024)), c(113))
})

test_that("`find_primes` works for numeric matrices", {
  A = matrix(
    c(1, 2, 3, 4, 5, 6, 7, 8, 9),
    nrow = 3, ncol = 3,
    byrow = TRUE
  )
  expect_equal(believe(A), c(7, 5, 3))
})