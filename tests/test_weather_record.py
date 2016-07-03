from unittest import TestCase
from unittest.mock import patch
from domain.weather_record import WeatherRecord

class TestWeatherRecord(TestCase):
	def test_should_flag_rainy_day_when_precipitation_beyond_limit(self):   
		weather_record = WeatherRecord(100, 85,23)    	
		self.assertTrue(weather_record.is_rainy())

	def test_should_flag_rainy_day_when_precipitation_below_limit(self):   
		weather_record = WeatherRecord(100, 85,12)    	
		self.assertFalse(weather_record.is_rainy())