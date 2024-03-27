from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def test_initialisation_with_correct_data(self):
        team = Team('Chelsea')
        self.assertEqual('Chelsea', team.name)
        self.assertEqual({}, team.members)

    def test_name_with_numbers_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            team = Team('@#Mimi123')
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_with_not_existing_member(self):
        team = Team('Chelsea')
        result = team.add_member(**{'Dimitar': 35, 'Peter': 30})
        self.assertTrue('Dimitar' in team.members)
        self.assertTrue('Successfully added: Dimitar, Peter', result)
        result = team.add_member(**{'Mimi': 33})
        self.assertEqual('Successfully added: Mimi', result)
        result = team.add_member(**{'Mimi': 33})
        self.assertEqual('Successfully added: ', result)

    def test_remove_player_with_valid_name(self):
        team = Team('Chelsea')
        team.add_member(**{'Dimitar': 35, 'Peter': 30})
        result = team.remove_member('Peter')
        self.assertEqual("Member Peter removed", result)
        self.assertFalse('Peter' in team.members)
        result = team.remove_member('Peter')
        expected = "Member with name Peter does not exist"
        self.assertEqual(expected, result)

    def test_gt_method_returns_proper_boolean(self):
        team = Team('Chelsea')
        other_team = Team('asd')
        team.add_member(**{'Dimitar': 35, 'Peter': 30, 'Julia': 32})
        other_team.add_member(**{'Mimi': 33})
        result = team > other_team
        self.assertEqual(True, result)

    def test_gt_method_with_false(self):
        other_team = Team('asd')
        team = Team('Chelsea')
        other_team.add_member(**{'Dimitar': 35, 'Peter': 30, 'Julia': 32})
        team.add_member(**{'Mimi': 33})
        result = team > other_team
        self.assertEqual(False, result)
        team.add_member(**{'Lili': 33, 'George': 35})
        result = team > other_team
        self.assertEqual(False, result)

    def test_len_method(self):
        team = Team('asd')
        result = len(team)
        self.assertEqual(0, result)
        team.add_member(**{'Mimi': 33})
        result = len(team)
        self.assertEqual(1, result)
        team.add_member(**{'Dimitar': 35, 'Peter': 30, 'Julia': 32})
        result = len(team)
        self.assertEqual(4, result)

    def test_add_method_creating_new_team(self):
        team = Team('Chelsea')
        other_team = Team('Liverpool')
        team.add_member(**{'Mimi': 33})
        other_team.add_member(**{'Dimitar': 35, 'Peter': 30, 'Julia': 32})
        members = {'Mimi': 33, 'Dimitar': 35, 'Peter': 30, 'Julia': 32}
        result = team + other_team
        self.assertEqual('ChelseaLiverpool', result.name)
        self.assertEqual(members, result.members)

    def test_str_method_returns_proper_string(self):
        team = Team('Chelsea')
        team.add_member(**{'Mimi': 33, 'Dimitar': 35, 'Peter': 30, 'Julia': 32, 'Angel': 35})
        result = str(team)
        expected = 'Team name: Chelsea\nMember: Angel - 35-years old\nMember: Dimitar - 35-years old\nMember: Mimi - ' \
                   '33-years old\nMember: Julia - 32-years old\nMember: Peter - 30-years old'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()