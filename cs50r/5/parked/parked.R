library("tidyverse")
input_text <- readLines(con <- file("abba.txt", encoding = "UTF-8"))

# Convert text to lowercase and split into words
words <- tolower(unlist(strsplit(input_text, "\\W+")))
words <- words[words != ""]

# Count frequency
word_freq <- table(words)
word_freq <- as.data.frame(word_freq)
colnames(word_freq) <- c("word", "n")

# Sort by frequency
word_freq <- word_freq [order(-word_freq$n), ]

word_freq <- word_freq |>
  filter(n > 2) |>
  mutate(word = reorder(word, n))

p <- ggplot(word_freq, aes(n, word)) +
  geom_col(fill = "deepskyblue4") +
  labs(x = NULL, y = NULL) +
  theme_classic()

ggsave(
  "lyrics.png",
  plot = p,
  width = 1200,
  height = 900,
  units = "px"
)