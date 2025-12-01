# Reads inputs
books <- read.csv("books.csv")
authors <- read.csv("authors.csv")


# 1 problem
# Find all books by Mia Morgan, it is only one title
books[books$author == "Mia Morgan", ]$title


# 2 problem
# Find all books written in 1613 about music, it is only one title
books[books$year == 1613 & books$topic == "Music", ]$title


# 3 problem
# Find all books written by Lysandra Silverleaf or Elena Petrova in 1775, it is only one title
books[books$year == 1775 & books$author %in% c("Lysandra Silverleaf", "Elena Petrova"), ]$title


# 4 problem
# Find all books about Art written in 1990 or 1992, it is only one title
books[books$topic == "Art" & books$year %in% c(1990, 1992), ]$title


# 5 problem
# Find all books with "Quantum Mechanics" in the title, it is only one title
books[grepl("Quantum Mechanics", books$title), ]$title


# 6 problem
# Find all books about Education written in 1700
# by author from Zenthia, it is only one title
books[books$year >= 1700 &
  books$year < 1800 &
  books$author %in% authors[authors$hometown == "Zenthia",]$author &
  books$topic == "Education", ]$title