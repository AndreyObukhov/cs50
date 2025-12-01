SELECT "birth_country" AS "Birth Country", "first_name" AS "First Name", "last_name" AS "Last Name" FROM "players"
WHERE "birth_country" != 'USA'
ORDER BY "birth_country", "first_name", "last_name";
