INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
SELECT 'update', 'admin', 'admin', (
    SELECT "password"
    FROM "users"
    WHERE "username" = 'admin'
), (
    SELECT "password"
    FROM "users"
    WHERE "username" = 'emily33'
);

UPDATE "users"
-- 'oops!' == '982c0381c279d139fd221fce974916e7' in MD5 Hash:
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- Delete last log from "user_logs"
DELETE FROM "user_logs"
WHERE "id" = (
    SELECT MAX("id")
    FROM "user_logs"
);
