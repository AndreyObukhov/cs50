-- Deletes prior tables if they exist
DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "schools";
DROP TABLE IF EXISTS "companies";
DROP TABLE IF EXISTS "user_and_user";
DROP TABLE IF EXISTS "company_and_user";
DROP TABLE IF EXISTS "school_and_user";

-- Creates tables with updated schema
CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT,
    "year" INTEGER,
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT,
    "location" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "user_and_user" (
    "id" INTEGER,
    "user1" TEXT NOT NULL,
    "user2" TEXT NOT NULL,
    "user1_id" INTEGER,
    "user2_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("user1_id") REFERENCES "users"("id"),
    FOREIGN KEY("user2_id") REFERENCES "users"("id")
);

CREATE TABLE "company_and_user" (
    "id" INTEGER,
    "user" TEXT NOT NULL,
    "company" TEXT NOT NULL,
    "start" NUMERIC,
    "end" NUMERIC,
    "title" TEXT,
    "user_id" INTEGER,
    "company_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "users"("id")
);

CREATE TABLE "school_and_user" (
    "id" INTEGER,
    "user" TEXT NOT NULL,
    "school" TEXT NOT NULL,
    "start" NUMERIC,
    "graduation" NUMERIC,
    "degree" TEXT,
    "user_id" INTEGER,
    "school_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);
