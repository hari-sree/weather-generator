# abstracts a very simple linear model of the form y = m*x + c
class LinearModel:	
	def __init__(self, slope, intercept):
		self.m = slope
		self.c = intercept

	def predict(self, x):
		return self.m * x + self.c

