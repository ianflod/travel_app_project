import unittest

from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Rome", "Italy", completed = False)

    def test_mark_completed_returns_true(self):
        self.city.mark_completed()
        self.assertEqual(True, self.city.completed)