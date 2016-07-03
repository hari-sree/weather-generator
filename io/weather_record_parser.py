import csv
from domain.weather_record import WeatherRecords,WeatherRecord

class WeatherRecordParser:
	def __init__(self, data_file):
		self.data_file = data_file
		self.columns_to_read = ['Mean TemperatureC', ' Mean Humidity', ' Mean Sea Level PressurehPa', 'Precipitationmm']

	def parse_weather_records(self):
		reader=csv.DictReader(open(self.data_file, 'r'))
		records = [ [ float(record[column]) for column in self.columns_to_read] for record in list(reader) ]		
		weather_records = WeatherRecords( list(map( lambda record: WeatherRecord(record[0], record[1], record[3]) , records)) )
		return weather_records
