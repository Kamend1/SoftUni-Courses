from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(50000, 3, True)

    def test_class_attributes(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500},
                         self.trip.DESTINATION_PRICES_PER_PERSON)

    def test_init_correctness(self):
        self.assertEqual(50000, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_property_travelers_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        expected = 'At least one traveler is required!'
        self.assertEqual(expected, str(ve.exception))

    def test_property_travelers_sets_correctly(self):
        self.trip.travelers = 5
        self.assertEqual(5, self.trip.travelers)

    def test_property_is_family_false(self):
        self.trip.is_family = ""
        self.assertFalse(self.trip.is_family)
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_book_trip_destination_not_valid(self):
        result = self.trip.book_a_trip("France")
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected, result)

    def test_book_trip_not_enough_budget(self):
        self.trip.budget = 5000

        result = self.trip.book_a_trip("New Zealand")
        expected = 'Your budget is not enough!'
        self.assertEqual(expected, result)

    def test_book_trip_correctly(self):
        self.trip.book_a_trip("New Zealand")
        self.assertEqual(29750, self.trip.budget)
        self.assertEqual({"New Zealand": 20250}, self.trip.booked_destinations_paid_amounts)

        self.trip.is_family = False
        result = self.trip.book_a_trip("Bulgaria")
        expected = 'Successfully booked destination Bulgaria! Your budget left is 28250.00'
        self.assertEqual(28250, self.trip.budget)
        self.assertEqual({"New Zealand": 20250, "Bulgaria": 1500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(expected, result)

    def test_booking_status_no_trips(self):
        result = self.trip.booking_status()
        expected = 'No bookings yet. Budget: 50000.00'
        self.assertEqual(expected, result)

    def test_booking_status_correct_message(self):
        self.trip.book_a_trip("New Zealand")
        self.assertEqual(29750, self.trip.budget)
        self.assertEqual({"New Zealand": 20250}, self.trip.booked_destinations_paid_amounts)

        self.trip.is_family = False
        self.trip.book_a_trip("Bulgaria")
        self.assertEqual(28250, self.trip.budget)
        self.assertEqual({"New Zealand": 20250, "Bulgaria": 1500}, self.trip.booked_destinations_paid_amounts)

        result = self.trip.booking_status()
        expected = (f"Booked Destination: Bulgaria\nPaid Amount: 1500.00\n"
                    f"Booked Destination: New Zealand\nPaid Amount: 20250.00\n"
                    f"Number of Travelers: 3\nBudget Left: 28250.00")
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
