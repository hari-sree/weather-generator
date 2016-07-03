from scipy import stats
from linear_model import LinearModel

class LinearLearner:
	def __init__(self, training_x,training_y):
		self.training_x = training_x
		self.training_y = training_y

	def learn(self):
		slope,intercept,r,p,s_err = stats.linregress(self.training_x, self.training_y)
		return LinearModel(slope, intercept)
