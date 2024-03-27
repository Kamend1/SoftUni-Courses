from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_name = "Kamen"
        self.notes = ["Test"]
        self.course_name = "Test IT"
        self.student = Student(self.student_name)
        self.student_with_courses = Student("Test2", {self.course_name: self.notes})

    def test_init(self):
        self.assertEqual(self.student_name, self.student.name)
        self.assertEqual("Test2", self.student_with_courses.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({self.course_name: self.notes}, self.student_with_courses.courses)

    def test_enroll_new_course_without_notes(self):
        expected_result = "Course has been added."
        course_name = "Test IT"
        notes = ["Test"]
        self.assertEqual(expected_result, self.student.enroll(course_name, notes, "N"))
        self.assertEqual([], self.student.courses[course_name])

    def test_enroll_new_course_with_notes(self):
        expected_result = "Course and course notes have been added."
        notes = ["Test"]
        course_name = "Test IT"
        self.assertEqual(expected_result, self.student.enroll(course_name, notes, ""))
        self.assertEqual(notes, self.student.courses[course_name])

    def test_enroll_new_course_with_notes_with_y_indicator(self):
        expected_result = "Course and course notes have been added."
        notes = ["Test"]
        course_name = "Test IT"
        self.assertEqual(expected_result, self.student.enroll(course_name, notes, "Y"))
        self.assertEqual(notes, self.student.courses[course_name])

    def test_course_already_added(self):
        expected_result = "Course already added. Notes have been updated."
        notes = ["Test1"]
        course_name = "Test IT"

        self.assertEqual(expected_result, self.student_with_courses.enroll(self.course_name, notes, ""))
        self.assertEqual(["Test", "Test1"], self.student_with_courses.courses[self.course_name])

    def test_add_notes_nonexisting_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Test 2", [])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_success(self):
        expected_result = "Notes have been updated"
        notes = []
        added_notes = "Test"
        course_name = "Test IT"
        self.student.enroll(course_name, notes, "N")
        self.assertEqual(expected_result, self.student.add_notes(course_name, added_notes))
        self.assertEqual([added_notes], self.student.courses[course_name])

    def test_leave_course_fail(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Test IT")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_success(self):
        course_name = "Test IT"
        notes = ["Test"]
        self.student.enroll(course_name, notes, "N")
        expected_result = "Course has been removed"
        self.assertEqual(expected_result, self.student.leave_course(course_name))


if __name__ == '__main__':
    main()
