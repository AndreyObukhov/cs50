SELECT "teams"."name"
FROM "teams"
JOIN "performances" ON "performances"."team_id" = "teams"."id"
JOIN "players" ON "players"."id" = "performances"."player_id"
WHERE "first_name" = 'Satchel' AND "last_name" = 'Paige'
GROUP BY "teams"."name";
