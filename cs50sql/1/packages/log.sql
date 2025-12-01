
-- *** The Lost Letter ***

-- Let's find all packages from 900 Somerville Avenue:

SELECT "id", "contents", "to_address_id" FROM "packages"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '900 Somerville Avenue'
);

-- As a resilt, we found four, one of which is
-- the Congratulatory letter with 'to_address_id' = 854

-- Let's find exact 'to_address' by its id:

SELECT "id", "address", "type" FROM "addresses" WHERE "id" = '854';

-- We found "address" = '2 Finnigan Street', so there was TYPO in delivery address

-- *** The Devious Delivery ***

-- Let's find all packages where "from_address_id" IS NULL:

SELECT "id", "contents", "to_address_id" FROM "packages" WHERE "from_address_id" IS NULL;

-- We found only one: "contents" = 'Duck debugger' with "to_address_id" = 50
-- Let's inspect package history:

SELECT * FROM "scans" WHERE "package_id" = 5098;

-- Last action was made on the address with "address_id" = 348
-- Let's find this address:

SELECT * FROM "addresses" WHERE "id" = 348;

-- We found address with "type" = 'Police Station'

-- *** The Forgotten Gift ***

-- Let's find the package:

SELECT "id", "contents", "to_address_id" FROM "packages"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = '109 Tileston Street'
);

-- We obtained: "contents" = 'Flowers' and "id" = 9523
-- Let's inspect package history:

SELECT "id", "driver_id", "action", "timestamp" FROM "scans" WHERE "package_id" = '9523';

-- Last action was made by driver with "driver_id" = 17
-- Let's find this driver:

SELECT "id", "name" FROM "drivers" WHERE "id" = 17;

-- This driver has "name" = Mikel
