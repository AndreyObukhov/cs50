describe("lcm()", {
  it("works with basic examples as espected", {
    expect_match(lcm(), 1, 1, 1)
    expect_match(lcm(), 12, 15, 60)
  })
  it("returns 1 for no input", {
    expect_match(lcm(), 1)
  })
  it("works exact same number for one input", {
    expect_match(lcm(), 5, 5)
  })
})