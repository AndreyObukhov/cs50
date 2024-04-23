-- Keep a log of any SQL queries you execute as you solve the mystery.

-- SQL query to see descriprion fo this particular crime.

SELECT description, id
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND year = 2021
AND street = "Humphrey Street";

-- Description is: Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time –
-- each of their interview transcripts mentions the bakery. id = 295

-- SQL query to see three mentioned inerviews.

SELECT transcript, name, id FROM interviews
WHERE month = 7 AND day = 28 AND year = 2021;

-- OUTPUT:
-- name: Emma id: 193 (according to the id, this interview was given much later then three main interviews.)
-- I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour. They never bought anything.

-- name: Raymond id: 163
-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- name: Eugene id: 162
-- I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- name: Ruth id: 161
-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

-- RUTH At fisrt we will investigate the Ruth's data.
-- SQL query to see bakery security logs:

SELECT id, license_plate, minute FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute < 26 and activity = "exit";

-- Intresting data for us is:
-- +-----+---------------+--------+
-- | id  | license_plate | minute |
-- +-----+---------------+--------+
-- | 260 | 5P2BI95       | 16     |
-- | 261 | 94KL13X       | 18     |
-- | 262 | 6P58WS2       | 18     |
-- | 263 | 4328GD8       | 19     |
-- | 264 | G412CB7       | 20     |
-- | 265 | L93JTIZ       | 21     |
-- | 266 | 322W7JE       | 23     |
-- | 267 | 0NTHK55       | 23     |
-- +-----+---------------+--------+

-- SQL query for searching people by their license plate:

SELECT id, name, license_plate FROM people
WHERE license_plate in
(SELECT license_plate FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute < 26 and activity = "exit");

-- The output we have:
-- +--------+---------+---------------+
-- |   id   |  name   | license_plate |
-- +--------+---------+---------------+
-- | 221103 | Vanessa | 5P2BI95       |
-- | 243696 | Barry   | 6P58WS2       |
-- | 396669 | Iman    | L93JTIZ       |
-- | 398010 | Sofia   | G412CB7       |
-- | 467400 | Luca    | 4328GD8       |
-- | 514354 | Diana   | 322W7JE       |
-- | 560886 | Kelsey  | 0NTHK55       |
-- | 686048 | Bruce   | 94KL13X       |
-- +--------+---------+---------------+

-- Next lets investigate Eugene's information.
-- SQL query for appropriate ATM transactions:

SELECT id, account_number, amount FROM atm_transactions
WHERE month = 7 AND day = 28 AND year = 2021
AND atm_location = "Leggett Street" AND transaction_type = "withdraw";

-- So, we have:
-- +-----+----------------+--------+
-- | id  | account_number | amount |
-- +-----+----------------+--------+
-- | 246 | 28500762       | 48     |
-- | 264 | 28296815       | 20     |
-- | 266 | 76054385       | 60     |
-- | 267 | 49610011       | 50     |
-- | 269 | 16153065       | 80     |
-- | 288 | 25506511       | 20     |
-- | 313 | 81061156       | 30     |
-- | 336 | 26013199       | 35     |
-- +-----+----------------+--------+

-- SQL query for people with these bank accounts:

SELECT DISTINCT(people.id), name, license_plate FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions
WHERE month = 7 AND day = 28 AND year = 2021
AND atm_location = "Leggett Street" AND transaction_type = "withdraw");

We have:
-- +--------+---------+---------------+
-- |   id   |  name   | license_plate |
-- +--------+---------+---------------+
-- | 395717 | Kenny   | 30G67EN       |
-- | 396669 | Iman    | L93JTIZ       |
-- | 438727 | Benista | 8X428L0       |
-- | 449774 | Taylor  | 1106N58       |
-- | 458378 | Brooke  | QX4YZN3       |
-- | 467400 | Luca    | 4328GD8       |
-- | 514354 | Diana   | 322W7JE       |
-- | 686048 | Bruce   | 94KL13X       |
-- +--------+---------+---------------+

-- Lets Intersect this set of people with set from bakery security logs:

SELECT id, name, phone_number FROM people
WHERE license_plate in
(SELECT license_plate FROM bakery_security_logs
WHERE month = 7 AND day = 28 AND year = 2021 AND hour = 10 AND minute < 26 and activity = "exit")
INTERSECT
SELECT people.id, name, phone_number FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions
WHERE month = 7 AND day = 28 AND year = 2021
AND atm_location = "Leggett Street" AND transaction_type = "withdraw");

-- We now have five suspects:
-- +--------+--------+----------------+
-- |   id   |  name  |  phone_number  |
-- +--------+--------+----------------+
-- | 396669 | Iman   | (829) 555-5269 |
-- | 467400 | Luca   | (389) 555-5198 |
-- | 514354 | Diana  | (770) 555-1861 |
-- | 686048 | Bruce  | (367) 555-5533 |
-- +--------+--------+----------------+

-- This people were exiting the bakery parking within ten minutes of the theft and also used ATM for withdrawing money.

-- Now lets investigate Raymond's data about "planning to take the earliest flight out of Fiftyville tomorrow":

SELECT id, caller, receiver, duration FROM phone_calls
WHERE month = 7 AND day = 28 AND year = 2021 AND duration <= 60
AND caller in ("(829) 555-5269", "(389) 555-5198", "(770) 555-1861", "(367) 555-5533");

-- We have:
-- +-----+----------------+----------------+----------+
-- | id  |     caller     |    receiver    | duration |
-- +-----+----------------+----------------+----------+
-- | 233 | (367) 555-5533 | (375) 555-8161 | 45       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 49       |
-- +-----+----------------+----------------+----------+

-- Now we can easily update set of suspects:

SELECT id, name, passport_number, phone_number FROM people
WHERE phone_number in ("(770) 555-1861", "(367) 555-5533");

-- We have:
-- +--------+--------+-----------------+----------------+
-- |   id   |  name  | passport_number |  phone_number  |
-- +--------+--------+-----------------+----------------+
-- | 514354 | Diana  | 3592750733      | (770) 555-1861 |
-- | 686048 | Bruce  | 5773159633      | (367) 555-5533 |
-- +--------+--------+-----------------+----------------+

-- Lets now investigate the fligts and find the earliest:
SELECT flights.id, hour, minute FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE airports.city = "Fiftyville" AND
month = 7 AND day = 29 AND year = 2021
ORDER BY hour, minute;

-- We have:
-- +----+------+--------+
-- | id | hour | minute |
-- +----+------+--------+
-- | 36 | 8    | 20     |
-- | 43 | 9    | 30     |
-- | 23 | 12   | 15     |
-- | 53 | 15   | 20     |
-- | 18 | 16   | 0      |
-- +----+------+--------+

--Finally, test found, which suspect bought a ticket for the earliest flight:
SELECT passport_number FROM passengers
WHERE passengers.flight_id = 36 and passport_number IN (3592750733, 5773159633);

-- It give us passport_number = 5773159633, which means Bruce is the thief.
-- He called to the number (375) 555-8161, so this person is his accomplice.
-- Lets found the accomplice:

SELECT name FROM people
WHERE phone_number = "(375) 555-8161";

-- At the end, query for city the thief escaped to:

SELECT city FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.id = 36;

-- It is New York City.
-- We have answered all the necessary questions.