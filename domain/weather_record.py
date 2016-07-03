import numpy as np

class WeatherRecord:
	def __init__(self, mean_temperature = 0, mean_humidity = 0, precipitation = 0):
		self.mean_temperature = mean_temperature
		self.mean_humidity = mean_humidity
		self.precipitation = precipitation

	def temperature(self):
		return self.mean_temperature

	def humidity(self):
		return self.mean_humidity

	def is_rainy(self):
		return self.precipitation > 15

	def __str__(self):
		return str( np.around(self.temperature()[0],1) ) + '|' + str(np.around(self.humidity()[0],1))

class WeatherRecords:
	def __init__(self,records):
		self.records = records

	def get_temperature_readings(self):
		return [ record.temperature() for record in self.records]

	def get_humidity_readings(self):
		return [ record.humidity() for record in self.records]

	def get_rainy_day_records(self):
		return WeatherRecords([record for record in self.records if record.is_rainy()])

	def get_sunny_day_records(self):
		return WeatherRecords([record for record in self.records if not record.is_rainy()])

	def temperature_mean(self):
		return np.array(self.get_temperature_readings()).mean()
	
	def temperature_standard_deviation(self):
		return np.array(self.get_temperature_readings()).std()		