from domain.city import City
import os
import sys
from datetime import date

DEFAULT_CITY = 'SYD'
DEFAULT_DAYS_COUNT = 10
DEFAULT_START_DATE = date.today()
DATA_DIRECTORY = 'data'

class Input:
	def __init__(self,sequence_count, city_data, start_date):
		self.sequence_count = sequence_count
		self.city_data = city_data
		self.start_date = start_date

class InputReader:
	def load_input_cities(self):
		test_file_lines = open('test_input.data','r').readlines()
		cities = [ City(test_line.strip().split('|')[0], test_line.strip().split('|')[1]) for test_line in test_file_lines]
		return cities

	def get_past_data_file_for_city(self, city):
		file_name = self.construct_data_file_name(city)
		if(os.path.isfile(file_name)):
			return file_name
		else:	
			return self.construct_data_file_name(DEFAULT_CITY)

	def get_sequence_count(self,):
		return int(sys.argv[1]) if(len(sys.argv) > 1) else DEFAULT_DAYS_COUNT

	def construct_data_file_name(self, city):
		file_name = city.get_code()+'.csv'
		return os.path.join(DATA_DIRECTORY, file_name)

	def load(self):
		cities = self.load_input_cities()
		city_data = {}
		for city in cities:
			city_data[city] = self.get_past_data_file_for_city(city)
			
		return Input(self.get_sequence_count(), city_data, DEFAULT_START_DATE)