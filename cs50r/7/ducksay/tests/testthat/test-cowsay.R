describe("cowsay()", {
  it("can print to the console with `cat`", {
    expect_output(cat(cowsay()))
  })
  it("can say hello to the world", {
    expect_match(cowsay(), "hello, world")
  })
  it("can say hello with a cow", {
    cow <- paste(
      "^__^",
      "(oo)\\_______",
      "(__)\\       )\\/\\",
      sep = "\n"
    )
    expect_match(cowsay(), cow, fixed = TRUE)
  })
  it("can say any given phrase", {
    expect_match(cowsay("moo!"), "moo!")
  })
})
