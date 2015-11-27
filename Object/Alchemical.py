from Object.AlchemicalColor import AlchemicalColor
from Object.AlchemicalSign import AlchemicalSign
from Object.AlchemicalSize import AlchemicalSize
class Alchemical:
	def __init__(self, color, sign, size):
		self.color = color
		self.sign = sign
		self.size = size

	def get_color(self):
			return self.color

	def get_sign(self):
			return self.sign

	def get_size(self):
			return self.size
