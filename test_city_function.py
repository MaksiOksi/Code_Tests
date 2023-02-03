import unittest
from city_function import get_city_info


class CityNameTestCase(unittest.TestCase):

    def test_city_country(self):
        city_info = get_city_info('lviv', 'ukraine')
        self.assertEqual(city_info, "Lviv,Ukraine")

    def test_city_country_population(self):
        city_info = get_city_info('lviv', 'ukraine')
        self.assertEqual(city_info, "Lviv,Ukraine")

if __name__ == '__main__':
    unittest.main
