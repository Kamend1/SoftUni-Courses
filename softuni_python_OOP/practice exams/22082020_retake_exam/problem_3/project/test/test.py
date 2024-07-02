from project.student_report_card import StudentReportCard
from unittest import TestCase, main

class TestStudentReportCard(TestCase):

    def setUp(self):
        self.rc = StudentReportCard("Test Student", 10)

    def test_correct_init(self):
        self.assertEqual("Test Student", self.rc.student_name)
        self.assertEqual(10, self.rc.school_year)
        self.assertEqual({}, self.rc.grades_by_subject)

    def test_property_empty_name_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.rc.student_name = ""

        expected = "Student Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_property_setter_name_works_ok(self):
        self.rc.student_name = "Kamen Dimitrov"
        self.assertEqual("Kamen Dimitrov", self.rc.student_name)

    def test_school_year_not_ok_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.rc.school_year = 2023

        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))

    def test_school_year_changes_ok(self):
        self.rc.school_year = 1
        self.assertEqual(1, self.rc.school_year)
        self.rc.school_year = 12
        self.assertEqual(12, self.rc.school_year)

    def test_add_grade_different_cases(self):
        self.rc.add_grade("Math", 6)
        self.assertEqual({"Math": [6]}, self.rc.grades_by_subject)
        self.rc.add_grade("Math", 4)
        self.assertEqual({"Math": [6, 4]}, self.rc.grades_by_subject)
        self.rc.add_grade("BEL", 5)
        self.assertEqual({"Math": [6, 4], "BEL": [5]}, self.rc.grades_by_subject)

    def test_average_grade_by_subject(self):
        expected = ''
        result = self.rc.average_grade_by_subject()
        self.assertEqual(expected, result)
        self.rc.add_grade("Math", 6)
        self.rc.add_grade("Math", 4)
        self.rc.add_grade("BEL", 5)
        expected = f"Math: 5.00\nBEL: 5.00"
        result = self.rc.average_grade_by_subject()
        self.rc.average_grade_by_subject()

    def test_average_grade_for_all_subjects(self):
        # result = self.rc.average_grade_for_all_subjects()
        # expected = "Average Grade: 0.00"
        # self.assertEqual(expected, result)
        self.rc.add_grade("Math", 6)
        self.rc.add_grade("Math", 4)
        self.rc.add_grade("BEL", 5)
        expected = "Average Grade: 5.00"
        result = self.rc.average_grade_for_all_subjects()
        self.assertEqual(expected, result)

    def test_correct_represent(self):
        expected = (f"Name: Test Student\n"
                    f"Year: 10\n"
                    f"----------\n"
                    f"Math: 5.00\nBEL: 5.00\n"
                    f"----------\n"
                    f"Average Grade: 5.00")
        self.rc.add_grade("Math", 6)
        self.rc.add_grade("Math", 4)
        self.rc.add_grade("BEL", 5)
        result = str(self.rc)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()