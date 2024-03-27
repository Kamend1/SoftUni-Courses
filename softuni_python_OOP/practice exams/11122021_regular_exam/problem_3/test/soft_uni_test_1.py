from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.first_team = Team("Juventus")
        self.second_team = Team("Barcelona")

    def test_init(self):
        self.assertEqual("Juventus", self.first_team.name)
        self.assertEqual({}, self.first_team.members)

    def test_name_setter_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.first_team.name = "!"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_setter(self):
        self.first_team.name = "Napoli"
        self.assertEqual("Napoli", self.first_team.name)

    def test_add_member(self):
        first_team_members = {"Chiellini": 37, "Morata": 29, "Chiesa": 24}
        result = self.first_team.add_member(**first_team_members)
        self.assertEqual("Successfully added: Chiellini, Morata, Chiesa", result)
        self.assertEqual({"Chiellini": 37, "Morata": 29, "Chiesa": 24}, self.first_team.members)
        more_members = {"test_member": 30, "Morata": 29}
        result = self.first_team.add_member(**more_members)
        self.assertEqual("Successfully added: test_member", result)
        self.assertEqual({"Chiellini": 37, "Morata": 29, "Chiesa": 24, "test_member": 30}, self.first_team.members)

    def test_remove_if_name_in_members(self):
        first_team_members = {"Chiellini": 37, "Morata": 29, "Chiesa": 24}
        self.first_team.add_member(**first_team_members)
        name = "Chiesa"
        result = self.first_team.remove_member(name)
        self.assertEqual(f"Member {name} removed", result)
        self.assertEqual({"Chiellini": 37, "Morata": 29}, self.first_team.members)

    def test_remove_if_name_not_in_members(self):
        first_team_members = {"Chiellini": 37, "Morata": 29, "Chiesa": 24}
        self.first_team.add_member(**first_team_members)
        name = "Ronaldo"
        result = self.first_team.remove_member(name)
        self.assertEqual(f"Member with name {name} does not exist", result)
        self.assertEqual({"Chiellini": 37, "Morata": 29, "Chiesa": 24}, self.first_team.members)

    def test__gt__true(self):
        first_team_members = {"Chiellini": 37, "Morata": 29, "Chiesa": 24}
        self.first_team.add_member(**first_team_members)
        second_team_members = {"Alves": 38, "Pique": 35}
        self.second_team.add_member(**second_team_members)
        self.assertEqual(True, self.first_team > self.second_team)

    def test__gt__false(self):
        first_team_members = {"Chiellini": 37, "Morata": 29}
        self.first_team.add_member(**first_team_members)
        second_team_members = {"Alves": 38, "Pique": 35, "Alba": 33}
        self.second_team.add_member(**second_team_members)
        self.assertEqual(False, self.first_team > self.second_team)

    def test__len__(self):
        first_team_members = {"Chiellini": 37, "Morata": 29}
        self.first_team.add_member(**first_team_members)
        self.assertEqual(2, len(self.first_team))

    def test__add__(self):
        first_team_members = {"Chiellini": 37, "Morata": 29}
        self.first_team.add_member(**first_team_members)
        second_team_members = {"Alves": 38, "Pique": 35}
        self.second_team.add_member(**second_team_members)
        new_football_team = self.first_team + self.second_team
        new_team_name = f"{self.first_team.name}{self.second_team.name}"
        new_team = Team(new_team_name)
        new_team.add_member(**self.first_team.members)
        new_team.add_member(**self.second_team.members)
        self.assertEqual(new_team_name, new_football_team.name)
        self.assertEqual(new_football_team.members, new_team.members)

    def test__str__(self):
        first_team_members = {"Chiellini": 37, "Morata": 29}
        self.first_team.add_member(**first_team_members)
        result = [f"Team name: {self.first_team.name}"]
        members = list(sorted(self.first_team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        self.assertEqual("\n".join(result), str(self.first_team))


if __name__ == "__main__":
    main()