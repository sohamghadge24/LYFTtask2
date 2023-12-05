import unittest

from Engine.CapuletEngine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 260434
        last_service_mileage = 20
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 32340
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())