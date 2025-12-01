SELECT "first_name", "last_name", "salary"/"H" AS "dollar per hit"
FROM "players"
JOIN "performances" ON "performances"."player_id" = "players"."id"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
WHERE "performances"."year" = "salaries"."year" AND
"salaries"."year" = 2001
AND "performances"."H" > 0
ORDER BY "dollar per hit", "first_name", "last_name"
LIMIT 10;
