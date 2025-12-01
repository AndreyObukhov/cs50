SELECT "salary"
FROM "salaries"
JOIN "players" ON "players"."id" = "salaries"."player_id"
JOIN "performances" ON "performances"."player_id" = "players"."id"
WHERE "HR" = (
    SELECT MAX("HR")
    FROM "performances"
    WHERE "year" = 2001
) AND
"salaries"."year" = 2001;
