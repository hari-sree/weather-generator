import numpy as np
import pdb
class NormalDistribution:
	def __init__(self, mean, sd):
		self.mean = mean
		self.sd = sd

	def get_sample(self):
		# pdb.set_trace()
		return np.random.normal(self.mean, self.sd, 1)