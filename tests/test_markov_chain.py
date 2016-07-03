from unittest import TestCase
from models.markov import MarkovChain

class TestMarkovChain(TestCase):
	def test_should_return_next_state_when_transition_probability_is_one(self):   
		markov_chain = MarkovChain([1,2], [[0,1],
										   [1,0]])
		next_state = markov_chain.forecast_next(1)
		self.assertEquals(2, next_state)

	def test_should_stay_in_current_state_when_transition_probability_is_zero(self):   
		markov_chain = MarkovChain([1,2], [[1,0],
										   [1,0]])
		next_state = markov_chain.forecast_next(1)
		self.assertEquals(1, next_state)