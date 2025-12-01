SELECT "city", COUNT("schools")
FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
HAVING COUNT("schools") <=3
ORDER BY COUNT("schools") DESC, "city";
