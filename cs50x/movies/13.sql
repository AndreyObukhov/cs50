-- SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT name FROM stars
JOIN movies ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE title IN
(SELECT title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE name = "Kevin Bacon" and birth = 1958)
AND name != "Kevin Bacon";