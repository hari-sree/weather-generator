from domain.weather_record import WeatherRecords,WeatherRecord
from domain.weather_reading import WeatherReading

class States:
	Rainy = 'Rainy'
	Sunny = 'Sunny'

class WeatherModel:
	def __init__(self,weather_markov_chain, humidity_model, rainy_normal_dist, sunny_normal_dist):
		self.weather_markov_chain = weather_markov_chain
		self.humidity_model = humidity_model

		self.state_temperature_dists = {
			States.Sunny : sunny_normal_dist,
			States.Rainy : rainy_normal_dist,
		}

	def generate_next_reading(self, previous_state, day):
		next_weather_type = self.weather_markov_chain.forecast_next(previous_state)
		temperature = self.state_temperature_dists[next_weather_type].get_sample()
		humidity = self.humidity_model.predict(temperature)

		return WeatherReading(next_weather_type, WeatherRecord(temperature, humidity), day )

	