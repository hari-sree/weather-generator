from markov import *
from linear_learner import *
from weather_model import *
from normal_distribution import *
import pdb

class WeatherModelCreater:
	def __init__(self,weather_records):
		self.weather_records = weather_records

	def create_model_from_data(self):
		states = [States.Rainy,States.Sunny]
		transitionProbabilities = [[0.8,0.2],
								   [0.6,0.4]]	
		weather_markov_chain = MarkovChain(states, transitionProbabilities)
		humidity_learner = LinearLearner(self.weather_records.get_temperature_readings(), self.weather_records.get_humidity_readings())
		humidity_model = humidity_learner.learn()

		rainy_records = self.weather_records.get_rainy_day_records()
		sunny_records = self.weather_records.get_sunny_day_records()
		
		rainy_sd = rainy_records.temperature_standard_deviation()
		sunny_sd = sunny_records.temperature_standard_deviation()

		rainy_mean = rainy_records.temperature_mean()
		sunny_mean = sunny_records.temperature_mean()

		rainy_normal_dist = NormalDistribution(rainy_mean,rainy_sd)
		sunny_normal_dist = NormalDistribution(sunny_mean,sunny_sd)
		

		weather_model = WeatherModel(weather_markov_chain, humidity_model, rainy_normal_dist, sunny_normal_dist)
		return weather_model

