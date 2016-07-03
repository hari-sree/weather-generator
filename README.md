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


Instructions to run :

	 i) Run tests
		pip install requirements-test.txt
		py.test
	ii) Run program 
		pip install requirements.txt
		python GenerateWeather.py

* Output format :
  City_Code|Coordinates|Date|Temperature|Humidity
