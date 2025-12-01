library(stringr)
library(testthat)

test_that("str_length is number of characters", {
  expect_equal(str_length("🦫"), 1)
  expect_equal(str_length("🐌🐺🐗🐝"), 4)
})

test_that("str_length of missing string is missing", {
  expect_equal(str_length(NA), NA_integer_)
  expect_equal(str_length(1), 1)
  expect_equal(str_length(c(NA, 1)), c(NA, 1))
  expect_equal(str_length("NA"), 2)
  expect_equal(str_length("Null"), 4)
  expect_equal(str_length("None"), 4)
})

test_that("str_length of vector is vector of lengths for each element", {
  expect_equal(str_length(c(1)), c(1))
  expect_equal(str_length(c(1, 2)), c(1, 1))
  expect_equal(str_length(c(1, 2, 3)), c(1, 1, 1))
})

test_that("data frame is not correct input", {
  df <- data.frame (
    Training = c("Strength", "Stamina", "Other"),
    Pulse = c(100, 150, 120),
    Duration = c(60, 30, 45)
  )
  expect_warning(str_length(df))
})