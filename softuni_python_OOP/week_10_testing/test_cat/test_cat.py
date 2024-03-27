from unittest import TestCase, main

# from test_cat.cat import Cat



class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Kotka")

    def test_init(self):
        self.assertEqual("Kotka", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_expected_size_increase_by_one_and_cat_fed_and_sleepy(self):
        expected_result = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.sleepy)
        self.assertTrue(self.cat.fed)
        self.assertEqual(expected_result, self.cat.size)

    def test_feed_cat_when_cat_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))
    def test_cat_is_fed_and_sleepy_sleeps_and_is_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_cat_is_not_fed_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

if __name__ == '__main__':
    main()