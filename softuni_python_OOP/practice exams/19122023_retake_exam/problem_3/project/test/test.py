from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestRobot(TestCase):

    def setUp(self):
        self.test_robot_mountain = ClimbingRobot("Mountain", "Test", 100, 100)
        self.test_robot_alpine = ClimbingRobot("Alpine", "Test1", 100, 100)
        self.test_robot_indoor = ClimbingRobot("Indoor", "Test2", 100, 100)
        self.test_robot_bouldering = ClimbingRobot("Bouldering", "Test3", 100, 100)

    def test_robot_has_attributes(self):
        self.assertTrue(hasattr(self.test_robot_mountain, "category"))
        self.assertTrue(hasattr(self.test_robot_mountain, "part_type"))
        self.assertTrue(hasattr(self.test_robot_mountain, "capacity"))
        self.assertTrue(hasattr(self.test_robot_mountain, "memory"))
        self.assertTrue(hasattr(self.test_robot_mountain, "installed_software"))

        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))

    def test_correct_init(self):
        robot = ClimbingRobot("Mountain", "Test", 100, 100)
        self.assertEqual("Mountain", robot.category)
        self.assertEqual("Test", robot.part_type)
        self.assertEqual(100, robot.capacity)
        self.assertEqual(100, robot.memory)
        self.assertEqual([], robot.installed_software)

    def test_category_setter_valid(self):
        valid_categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        for category in valid_categories:
            with self.subTest(category=category):
                self.test_robot_mountain.category = category
                self.assertEqual(self.test_robot_mountain.category, category)


    def test_incorrect_category(self):
        with self.assertRaises(ValueError) as ve:
            wrong_category = ClimbingRobot("Field", "Test4", 100, 100)

        expected = "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']"
        self.assertEqual(expected, str(ve.exception))

    def test_get_used_capacity_empty(self):
        expected = sum(s['capacity_consumption'] for s in self.test_robot_mountain.installed_software)
        result = self.test_robot_mountain.get_used_capacity()

        self.assertEqual(expected, result)

    def test_get_used_capacity_installed(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}
        self.test_robot_mountain.install_software(software)
        expected = 40
        result = self.test_robot_mountain.get_used_capacity()
        self.assertEqual(expected, result)

    def test_get_available_capacity_empty(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}
        self.test_robot_mountain.install_software(software)
        expected = 60
        result = self.test_robot_mountain.get_available_capacity()
        self.assertEqual(expected, result)

    def test_get_available_capacity(self):
        self.test_robot_mountain.installed_software = [{'capacity_consumption': 30}]
        self.assertEqual(self.test_robot_mountain.get_available_capacity(), 70)

    def test_get_used_memory_empty(self):
        expected = sum(s['memory_consumption'] for s in self.test_robot_mountain.installed_software)
        result = self.test_robot_mountain.get_used_memory()
        self.assertEqual(expected, result)

    def test_get_used_memory_full(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}
        self.test_robot_mountain.install_software(software)
        expected = sum(s['memory_consumption'] for s in self.test_robot_mountain.installed_software)
        result = self.test_robot_mountain.get_used_memory()
        self.assertEqual(expected, result)

    def test_get_available_memory_empty(self):
        expected = self.test_robot_mountain.memory - self.test_robot_mountain.get_used_memory()
        result = self.test_robot_mountain.get_available_memory()
        self.assertEqual(expected, result)

    def test_get_available_memory_full(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}
        self.test_robot_mountain.install_software(software)
        expected = self.test_robot_mountain.memory - self.test_robot_mountain.get_used_memory()
        result = self.test_robot_mountain.get_available_memory()
        self.assertEqual(expected, result)

    def test_install_software_cannot_install_less_capacity(self):
        software = {"name": "Test", "capacity_consumption": 120, "memory_consumption": 40}
        result = self.test_robot_mountain.install_software(software)
        expected = "Software 'Test' cannot be installed on Mountain part."
        self.assertEqual(expected, result)

    def test_install_software_install_equal_capacity(self):
        software = {"name": "Test", "capacity_consumption": 100, "memory_consumption": 40}
        result = self.test_robot_mountain.install_software(software)
        expected = "Software 'Test' successfully installed on Mountain part."
        self.assertEqual(expected, result)

    def test_install_software_cannot_install_less_memory(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 120}
        result = self.test_robot_mountain.install_software(software)
        expected = "Software 'Test' cannot be installed on Mountain part."
        self.assertEqual(expected, result)

    def test_install_software_install_equal_memory(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 100}
        result = self.test_robot_mountain.install_software(software)
        expected = "Software 'Test' successfully installed on Mountain part."
        self.assertEqual(expected, result)

    def test_install_software_successful(self):
        software = {"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}
        result = self.test_robot_mountain.install_software(software)
        expected = "Software 'Test' successfully installed on Mountain part."
        self.assertEqual(expected, result)
        self.assertEqual([{"name": "Test", "capacity_consumption": 40, "memory_consumption": 40}], self.test_robot_mountain.installed_software)



if __name__ == '__main__':
    main()