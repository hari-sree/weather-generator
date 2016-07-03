class WeatherReading:
	def __init__(self, weather_type, reading, day):
		self.weather_type = weather_type
		self.reading = reading
		self.day = day

	def get_weather_type(self):
		return self.weather_type

	def __str__(self):
		return str(self.day) + '|' +self.weather_type + '|' + str(self.reading)