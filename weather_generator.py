import random
from models.weather_model import WeatherModel,States
from datetime import timedelta

class WeatherGenerator:
	def __init__(self, city, weather_model):
		self.city = city
		self.weather_model = weather_model

	def generate_weather_sequence(self, no_days, start_date):
		weather_sequence = []
		states = [States.Rainy,States.Sunny]
		current_state = random.choice(states)
		current_day = start_date
		for day in range(no_days):
			next_reading = self.weather_model.generate_next_reading(current_state, current_day)	
			weather_sequence.append(next_reading)
			current_state = next_reading.get_weather_type()
			current_day = current_day + timedelta(days=1)
			
		return weather_sequence
