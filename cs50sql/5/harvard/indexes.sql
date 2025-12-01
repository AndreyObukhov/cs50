CREATE INDEX "enrolled_by_student" ON "enrollments" ("student_id");

CREATE INDEX "enrolled_by_course" ON "enrollments" ("course_id");

CREATE INDEX "courses_by_semestr" ON "courses" ("semester");

CREATE INDEX "satisfies_by_course" ON "satisfies" ("course_id");
