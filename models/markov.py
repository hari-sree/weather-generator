import numpy as np
import random 

class MarkovChain:
	def __init__(self, states, transition_probabilities):
		self.states = states
		self.transition_probabilities = transition_probabilities
		
	def forecast_next(self, previous_state):
		transition_pos = self.states.index(previous_state)
		next_state = np.random.choice(self.states, p=self.transition_probabilities[transition_pos])
		return next_state