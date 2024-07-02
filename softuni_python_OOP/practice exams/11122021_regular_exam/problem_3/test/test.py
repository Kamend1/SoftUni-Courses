from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self):
        self.test_team = Team("Test")
        self.test_other_team = Team("Other")

    def test_init_works_correctly(self):
        self.assertEqual("Test", self.test_team.name)
        self.assertEqual({}, self.test_team.members)

    def test_setter_raises_error_for_name(self):
        with self.assertRaises(ValueError) as ve:
            self.wrong_name = Team("!")

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_name_setter(self):
        team = Team("TestTest")
        self.assertEqual("TestTest", team.name)

    def test_add_members_override(self):
        members_to_add = {"Pesho": 10, "Gosho": 20}
        result = self.test_team.add_member(**members_to_add)
        expected_result = "Successfully added: Pesho, Gosho"
        self.assertEqual(expected_result, result)
        self.assertEqual(members_to_add, self.test_team.members)
        more_members = {"Pesho": 23, "Tosho": 15}
        result = self.test_team.add_member(**more_members)
        expected_result = "Successfully added: Tosho"
        expected_members = {"Pesho": 10, "Gosho": 20, "Tosho": 15}
        self.assertEqual(expected_result, result)
        self.assertEqual(expected_members, self.test_team.members)

    def test_add_members(self):
        members_to_add = {"Pesho": 10, "Gosho": 20}
        result = self.test_team.add_member(**members_to_add)
        expected_result = "Successfully added: Pesho, Gosho"
        self.assertEqual(expected_result, result)
        self.assertEqual(members_to_add, self.test_team.members)

    def test_add_members_empty_dictionary(self):
        members_to_add = {}
        result = self.test_team.add_member(**members_to_add)
        expected_result = "Successfully added: "
        self.assertEqual(expected_result, result)
        self.assertEqual({}, self.test_team.members)

    def test_remove_member_success(self):
        members_to_add = {"Pesho": 10, "Gosho": 20}
        self.test_team.add_member(**members_to_add)
        result = self.test_team.remove_member("Pesho")
        expected_result = "Member Pesho removed"
        members_to_check = {"Gosho": 20}
        self.assertEqual(expected_result, result)
        self.assertEqual(members_to_check, self.test_team.members)

    def test_remove_member_name_does_not_exist(self):
        result = self.test_team.remove_member("Tosho")
        expected_result = "Member with name Tosho does not exist"
        self.assertEqual(expected_result, result)
        self.assertEqual({}, self.test_team.members)

    def test_greater_then_method_return_false(self):
        members_to_add_1 = {"Pesho": 10, "Gosho": 20}
        members_to_add_2 = {"Tosho": 15}
        self.test_other_team.add_member(**members_to_add_1)
        self.assertEqual(False, self.test_team > self.test_other_team)
        self.test_team.add_member(**members_to_add_2)
        self.assertEqual(False, self.test_team > self.test_other_team)

    def test_greater_then_method_return_true(self):
        members_to_add_1 = {"Pesho": 10, "Gosho": 20}
        members_to_add_2 = {"Tosho": 15}
        self.test_team.add_member(**members_to_add_1)
        self.assertEqual(True, self.test_team > self.test_other_team)
        self.test_other_team.add_member(**members_to_add_2)
        self.assertEqual(True, self.test_team > self.test_other_team)

    def test_greater_then_equal_returns_false_if_equal_lengths(self):
        members_to_add_1 = {"Pesho": 10}
        members_to_add_2 = {"Tosho": 15}
        self.test_team.add_member(**members_to_add_1)
        self.test_other_team.add_member(**members_to_add_2)
        self.assertEqual(False, self.test_team > self.test_other_team)

    def test_len_method(self):
        self.assertEqual(0, len(self.test_team))
        members_to_add = {"Pesho": 10, "Gosho": 20}
        self.test_team.add_member(**members_to_add)
        self.assertEqual(2, len(self.test_team))

    def test_add_method_concatenate_two_instances(self):
        members_to_add = {"Tosho": 10}
        members_to_add_other = {"Pesho": 10, "Gosho": 20}
        self.test_team.add_member(**members_to_add)
        self.test_other_team.add_member(**members_to_add_other)
        members = {"Tosho": 10, "Pesho": 10, "Gosho": 20}
        new_team = self.test_team + self.test_other_team
        self.assertEqual("TestOther", new_team.name)
        self.assertEqual(members, new_team.members)

    def test_string_method_for_class(self):
        members = {"Tosho": 10, "Pesho": 10, "Gosho": 20}
        expected_result = ("Team name: Test" +
                           "\n" + "Member: Gosho - 20-years old" +
                           "\n" + "Member: Pesho - 10-years old" +
                           "\n" + "Member: Tosho - 10-years old"
                           )
        self.test_team.add_member(**members)
        self.assertEqual(expected_result, str(self.test_team))


if __name__ == '__main__':
    main()
