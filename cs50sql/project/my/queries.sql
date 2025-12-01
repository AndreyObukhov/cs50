-- Add some counties to the corresponding table
INSERT INTO "countries" ("name")
VALUES
('USA'),
('Spain'),
('France'),
('Switzerland');


-- Add new suppliers
INSERT INTO "suppliers" ("name", "country_id")
VALUES ('French Wines Inc.', 3),
('Spanish Fruits Ltd.', 2);


-- Add new food items with their quantities
INSERT INTO "items" ("name", "sup_id")
VALUES
('Cabernet Sauvignon', 1),
('Oranges', 2);


-- Add new quantities
INSERT INTO "quantities" ("quantity", "units", "item_id")
VALUES
(50, 'bottle', 1),
(1000, 'kg', 2);


-- Add new expiration dates
INSERT INTO "expirations" ("date", "item_id")
VALUES
('2027-01-01', 1),
('2024-11-01', 2);


-- Find all items currently on the market with expiration dates, ordered by soonest expirations
SELECT "items"."name" AS "Product", "expirations". "date" AS "Best before"
FROM "items"
JOIN "expirations" ON "expirations"."item_id" = "items"."id"
ORDER BY "Best before";


-- Find all suppliers with countries they are from
SELECT "suppliers"."name" AS "Name", "from" AS "Partnership from", "countries"."name" AS "Country"
FROM "suppliers"
JOIN "countries" ON "countries"."id" = "suppliers"."country_id";


-- Create VIEW for all current items with their quantities, expirations dates and suppliers
CREATE VIEW "products" AS
SELECT
    "items"."name" AS "product",
    "suppliers"."name" AS "supplier",
    "units",
    "quantity",
    "date" AS "best before"
FROM "items"
JOIN "quantities" ON "quantities"."item_id" = "items"."id"
JOIN "expirations" ON "expirations"."item_id" = "items"."id"
JOIN "suppliers" ON "suppliers"."id" = "items"."sup_id";


SELECT * FROM "products";
