from unittest import TestCase
from unittest.mock import patch
from models.linear_model import LinearModel

class TestLinearModel(TestCase):
	def test_should_return_identity_values_for_slope_one_and_intercept_zero(self):   
		linear_model = LinearModel(1, 0)    	
		self.assertEquals(11, linear_model.predict(11))

