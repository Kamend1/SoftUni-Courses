from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Kamen", 10, 200.5, 50.5)

    def test_correct_init(self):
        self.assertEqual("Kamen", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(200.5, self.hero.health)
        self.assertEqual(50.5, self.hero.damage)

    def test_battle_self_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_self_health_is_zero_or_below_valueerror(self):
        self.hero.health = 0
        new_hero = Hero("Test", 0, 100, 100)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(new_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_is_zero_or_below_valueerror(self):
        new_hero = Hero("Test", 0, 0, 100)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(new_hero)

        self.assertEqual("You cannot fight Test. He needs to rest", str(ve.exception))

    def test_battle_draw_output(self):
        new_hero = Hero("Test", 3, 100, 100)
        expected_result = "Draw"

        self.assertEqual(expected_result, self.hero.battle(new_hero))

    def test_battle_enemy_wins(self):
        new_hero = Hero("Test", 3, 3000, 100)
        expected_result = "You lose"
        self.assertEqual(expected_result, self.hero.battle(new_hero))
        self.assertEqual(4, new_hero.level)
        self.assertEqual(2500.0, new_hero.health)
        self.assertEqual(105, new_hero.damage)

    def test_battle_hero_wins(self):
        new_hero = Hero("Test", 0, 10, 100)
        expected_result = "You win"
        self.assertEqual(expected_result, self.hero.battle(new_hero))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(205.5, self.hero.health)
        self.assertEqual(55.5, self.hero.damage)


    def test_correct_string_output(self):
        expected_result = "Hero Kamen: 10 lvl" + "\n" + "Health: 200.5" + "\n" + "Damage: 50.5" + "\n"

        self.assertEqual(expected_result, str(self.hero))

if __name__ == '__main__':
    main()