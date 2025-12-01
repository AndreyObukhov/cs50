SELECT "first_name", "last_name"
FROM "players"
WHERE "id" IN (
    SELECT "players"."id"
    FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    WHERE "performances"."year" = "salaries"."year"
        AND "salaries"."year" = 2001
        AND "H" > 0
    ORDER BY "salary" / "H", "last_name"
LIMIT 10)

AND "id" IN (
    SELECT "players"."id"
    FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    WHERE "performances"."year" = "salaries"."year"
        AND "salaries"."year" = 2001
        AND "RBI" > 0
    ORDER BY "salary" / "RBI", "last_name"
LIMIT 10)

ORDER BY "players"."id", "last_name";
