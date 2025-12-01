describe("prime()", {
  it("works with basic examples as espected", {
    expect_match(prime(), 1, FALSE)
    expect_match(prime(), 2, TRUE)
    expect_match(prime(), 3, TRUE)
  })
  it("returns FALSE for no input", {
    expect_match(prime(), FALSE)
  })
  it("works for bigger numbers too", {
    expect_match(prime(),
                 359334085968622831041960188598043661065388726959079837,
                 TRUE)
  })
})