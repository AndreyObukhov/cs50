CREATE VIEW "june_vacancies" AS
SELECT "listings"."id", "property_type", "host_name", COUNT("listings"."id") AS "days_vacant"
FROM "listings"
JOIN "availabilities" ON "availabilities"."listing_id" = "listings"."id"
WHERE "availabilities"."date" >= '2023-06-01' AND "availabilities"."date" < '2023-07-01' AND "available" = 'TRUE'
GROUP BY "listings"."id";
