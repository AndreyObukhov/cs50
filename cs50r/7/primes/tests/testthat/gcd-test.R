describe("gcd()", {
  it("works with basic examples as espected", {
    expect_match(gcd(), 1, 1, 1)
    expect_match(gcd(), 18, 48, 6)
  })
  it("returns 1 for no input", {
    expect_match(gcd(), 1)
  })
  it("works exact same number for one input", {
    expect_match(gcd(), 5, 5)
  })
})