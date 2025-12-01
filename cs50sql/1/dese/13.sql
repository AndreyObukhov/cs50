SELECT "name", "dropped"
FROM "schools"
JOIN "graduation_rates" ON "graduation_rates"."school_id" = "schools"."id"
ORDER BY "dropped" DESC LIMIT 10;
