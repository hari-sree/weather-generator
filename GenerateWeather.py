from io.weather_record_parser import WeatherRecordParser
from models.weather_model_creator import WeatherModelCreater
from weather_generator import WeatherGenerator
from io.input_reader import InputReader

def print_sequence(city, weather_sequence):
	for weather_reading in weather_sequence:
		print(str(city) + '|'+ str(weather_reading))
		
if __name__=='__main__':
	input_args = InputReader().load()

	for city in input_args.city_data.keys():				
		weather_record_parser = WeatherRecordParser( input_args.city_data[city] )
		weather_records = weather_record_parser.parse_weather_records()
		weather_model_creator = WeatherModelCreater(weather_records)
		weather_model = weather_model_creator.create_model_from_data()

		weather_generator = WeatherGenerator(city, weather_model)
		weather_sequence = weather_generator.generate_weather_sequence(input_args.sequence_count, input_args.start_date)
		print_sequence(city, weather_sequence)

