-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "passengers";
DROP TABLE IF EXISTS "checkins";
DROP TABLE IF EXISTS "airlines";
DROP TABLE IF EXISTS "flights";

-- Creates tables with updated schema
CREATE TABLE "passengers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "age" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "airlines" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT NOT NULL CHECK("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    PRIMARY KEY("id")
);

CREATE TABLE "flights" (
    "id" INTEGER
    "number" INTEGER NOT NULL,
    "airline_id" INTEGER NOT NULL,
    "from" TEXT NOT NULL,
    "to" TEXT NOT NULL,
    "departure" NUMERIC NOT NULL,
    "arrival" NUMERIC NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);

CREATE TABLE "checkins" (
    "id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "passenger_id" INTEGER NOT NULL,
    "flight_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id"),
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id")
);
