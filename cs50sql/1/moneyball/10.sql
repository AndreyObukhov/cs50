SELECT "first_name", "last_name", "salaries"."salary", "salaries"."year", "HR"
FROM "players"
JOIN "performances" ON "performances"."player_id" = "players"."id"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
WHERE "performances"."year" = "salaries"."year"
ORDER BY "players"."id", "performances"."year" DESC, "performances"."HR" DESC, "salary" DESC;
