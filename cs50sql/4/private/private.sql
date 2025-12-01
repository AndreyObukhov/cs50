CREATE TABLE "cipher" (
    "id" INTEGER,
    "first" INTEGER,
    "second" INTEGER,
    "third" INTEGER,
    PRIMARY KEY("id")
);

INSERT INTO "cipher" ("first", "second", "third")
VALUES
(14, 98, 4),
(114, 3, 5),
(618, 72, 9),
(630, 7, 3),
(932, 12, 5),
(2230, 50, 7),
(2346, 44, 10),
(3041, 14, 5);

CREATE VIEW "important_sentences" AS
SELECT "id", "sentence" FROM "sentences"
WHERE "id" IN (
    SELECT "first"
    FROM "cipher"
)
ORDER BY "id";

CREATE VIEW "combined" AS
SELECT "sentence", "second", "third" FROM "important_sentences"
JOIN "cipher" ON "cipher"."first" = "important_sentences"."id"
ORDER BY "cipher"."id";

CREATE VIEW "message" AS
SELECT substr("sentence", "second", "third") AS "phrase" FROM "combined";
