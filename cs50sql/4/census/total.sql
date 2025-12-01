CREATE VIEW "total" AS
SELECT SUM("families") AS "families",
SUM("households") AS "households",
SUM("population") AS "population",
SUM("male") AS "male",
SUM("families") AS "female"
FROM "census";
