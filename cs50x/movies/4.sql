-- SQL query to determine the number of movies with an IMDb rating of 10.0.

SELECT COUNT(title) FROM movies WHERE id in (SELECT movie_id FROM ratings WHERE rating = 10.0);
-- SELECT COUNT(title) FROM movies JOIN ratings on movies.id = ratings.movie_id WHERE rating = 10.0;