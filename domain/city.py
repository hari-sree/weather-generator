class City:
	def __init__(self, code, coordinates):
		self.code = code
		self.coordinates = coordinates
	def get_code(self):
		return self.code
	def __str__(self):
		return str(self.code) + '|' + str(self.coordinates)