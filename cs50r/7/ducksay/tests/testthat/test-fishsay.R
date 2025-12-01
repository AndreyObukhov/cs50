describe("fishsay()", {
  it("can print to the console with `cat`", {
    expect_output(cat(fishsay()))
  })
  it("can say hello to the world", {
    expect_match(fishsay(), "hello, world")
  })
  it("can say hello with a fish", {
    fish <- paste(
      " ____ ",
      "(o   \\",
      " \\   / ",
      "  \\ /  ",
      "  ( )  ",
      sep = "\n"
    )
    expect_match(fishsay(), fish, fixed = TRUE)
  })
  it("can say any given phrase", {
    expect_match(fishsay("blub blub!"), "blub blub!")
  })
})
