-- Creates a temporally table to store imported data
CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" NUMERIC,
    "lat" REAL,
    "long" REAL
);

-- Imports into a temporary table using a meteorites.csv
.import --csv --skip 1 meteorites.csv meteorites_temp

DELETE FROM "meteorites_temp"
WHERE "nametype" = 'Relict';

UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = "";

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = "";

UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = "";

UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = "";

CREATE TABLE "meteorites" (
    "id" INTEGER,
    "name" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" NUMERIC,
    "lat" REAL,
    "long" REAL,
    PRIMARY KEY("id")
);

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", ROUND("mass", 2), "discovery", "year", ROUND("lat", 2), ROUND("long", 2)
FROM "meteorites_temp"
ORDER BY "year", "name";

-- Deletes temporary table
DROP TABLE "meteorites_temp";
