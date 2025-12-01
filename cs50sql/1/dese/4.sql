SELECT "city", COUNT("schools")
FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
ORDER BY COUNT("schools") DESC, "city" LIMIT 10;
