-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "quantities";
DROP TABLE IF EXISTS "expirations";
DROP TABLE IF EXISTS "items";
DROP TABLE IF EXISTS "suppliers";
DROP TABLE IF EXISTS "countries";
DROP INDEX IF EXISTS "item_name_search";
DROP INDEX IF EXISTS "countries_search";
DROP VIEW IF EXISTS "products";


-- Represent countries of the suppliers
CREATE TABLE "countries" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);


-- Represent suppliers of the food
CREATE TABLE "suppliers" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    -- From where partnership with this current supplier started
    "from" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "country_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("country_id") REFERENCES "countries"("id")
);


-- Represent items currently on the food market
CREATE TABLE "items" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "arrived" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "sup_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("sup_id") REFERENCES "suppliers"("id")
);


-- Represent expiration dates for the items
CREATE TABLE "expirations" (
    "id" INTEGER,
    "date" NUMERIC NOT NULL,
    "item_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("item_id") REFERENCES "items"("id")
);


-- Represent items quantity
CREATE TABLE "quantities" (
    "id" INTEGER,
    "quantity" INTEGER NOT NULL,
    "units" TEXT NOT NULL,
    "item_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("item_id") REFERENCES "items"("id")
);

-- Create indexes to speed common searches
CREATE INDEX "item_name_search" ON "items" ("name");
CREATE INDEX "countries_search" ON "countries" ("name");
CREATE INDEX "suppliers_search" ON "suppliers" ("name");
