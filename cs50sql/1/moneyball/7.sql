SELECT "first_name", "last_name"
FROM "salaries"
JOIN "players" ON "players"."id" = "salaries"."player_id"
WHERE "salary" = (
    SELECT MAX("salary")
    FROM "salaries"
)
ORDER BY "salary" DESC;
