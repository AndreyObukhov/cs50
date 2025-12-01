-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "ingredients";
DROP TABLE IF EXISTS "donuts";
DROP TABLE IF EXISTS "receipts";
DROP TABLE IF EXISTS "orders";
DROP TABLE IF EXISTS "customers";
DROP TABLE IF EXISTS "customers_and_orders";

-- Creates tables with updated schema

CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "price" REAL,
    "price_per_unit" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "gluten-free" INTEGER,
    "price" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "receipts" (
-- Boolean variable: 1 if ingredient is needed for particular donut.
    "is needed" INTEGER NOT NULL,
    "ingredient_id" INTEGER,
    "donut_id" INTEGER,
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
    PRIMARY KEY("ingredient_id", "donut_id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "orders" (
-- One row stands for one donut in the order.
-- So, for more than one donut in the order table will contain more lines
-- with different ids and same number.
    "id" INTEGER,
    "number" INTEGER,
    "donut" TEXT NOT NULL,
    "customer_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);
