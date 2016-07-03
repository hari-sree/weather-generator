# Weather-generator
##### Generate reasonably realistic weather sequences
Language : Python 2.7 

* I. External libraries used in the solution : 
	* Numpy 
		* for manipulation of the datasets
		* random sampling from the transition probabilities of the markov chain with random.choice function
		* random sampling from the normal distribution
	* Scipy 
		* for parameter estimation of the linear model using simple linear regression
	* Pytest : for unit tests

*  II. General(and weak) relations between weather variables utilised in the toy model :
	* Precipitation inversely proportional to Temperature 
	* Relative Humidity inversely proportional to Temperature (water holding capacity of air increases with temperature thereby reducing rh)
	* Pressure inversely proportional to Elevation 

* III. Model details / approach taken :
	* A two state Markov chain for modelling the time evolution of weather .
	* Once the weather type is sampled from the markov chain , temperature is generated from a normal distribution with mean & standard deviation calculated from the previous year data (Temperature assumed to be normally distributed , which is a simplifying assumption)
	* Humidity is inversely proportional to Temperature (See II) .This is modeled using a linear model whose parameters are calculated from previous year data using linear regression 

* IV. Further Improvements :
	* Estimating Markov chain transition probabilities from data	
	* Add more states to the chain like Cloudy / Snowy etc
	* Use of time series models like Moving Average/autoregressive models(ARIMA) for better modelling of weather variables
	* Better modelling of temperature by including more physical parameters
	* Including topographical features of the place into the model explicitly

* V. Notes
	* Data from 5 cities are included 
	* test_input file contains the city names for which weather has to be generated. If the corresponding city's previous year weather data is missing, Sydneys (SYD) data file will be used for parameter estimation

Instructions to run :

	 i) Run tests
		pip install -r requirements-test.txt
		py.test 'tests'
	ii) Run program 
		pip install -r requirements.txt
		python GenerateWeather.py
		        or
		python GenerateWeather.py |sequence_length|
		
		* Note : Default Sequence length is 10

* Output format :
  City_Code|Coordinates|Date|Temperature|Humidity


* Sample Output :
~~~
PER|-31.56,115.58,20|2016-07-03|Sunny|25.2|46.8
PER|-31.56,115.58,20|2016-07-04|Rainy|12.3|70.5
PER|-31.56,115.58,20|2016-07-05|Sunny|14.1|67.3
ADL|-34.56,138.31,30|2016-07-03|Rainy|20.8|71.4
ADL|-34.56,138.31,30|2016-07-04|Rainy|28.0|76.2
ADL|-34.56,138.31,30|2016-07-05|Sunny|27.6|75.9
SYD|-33.86,151.12,39|2016-07-03|Sunny|11.6|63.3
SYD|-33.86,151.12,39|2016-07-04|Rainy|20.7|64.4
SYD|-33.86,151.12,39|2016-07-05|Rainy|17.0|63.9
DRW|-12.24,130.52,34|2016-07-03|Sunny|26.4|64.0
DRW|-12.24,130.52,34|2016-07-04|Rainy|26.9|65.2
DRW|-12.24,130.52,34|2016-07-05|Sunny|30.2|74.4
BNE|-27.23,153.07,35|2016-07-03|Rainy|25.8|74.7
BNE|-27.23,153.07,35|2016-07-04|Rainy|25.2|74.3
BNE|-27.23,153.07,35|2016-07-05|Rainy|21.4|71.8
