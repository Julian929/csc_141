def get_city_country(city, country, population=''):
    """Return formatted city, country pair."""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()

import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city, country pairs like 'santiago', 'chile', work?"""
        formatted_city_country = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago', 'Chile')

    def test_city_country(self):
        """Test that optional population argument works properly."""
        formatted_city_country = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - Population 500000')

if __name__ == '__main__':
    unittest.main()