from unittest import TestCase
from domain.weather_record import WeatherRecord
from domain.weather_reading import WeatherReading
from datetime import date

class TestWeatherReading(TestCase):
	def test_should_give_correct_string_format(self):   
		weather_record = WeatherRecord([100], [85],23)    	
		weather_reading = WeatherReading('Rainy',weather_record, date(2015,1,14))
		self.assertEquals('2015-01-14|Rainy|100|85' , str(weather_reading))