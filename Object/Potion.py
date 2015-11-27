from Object.Ingredient import Ingredient
class Potion:
	def __init__(self, ingredient_one, ingredient_two, potion_color, potion_sign):
		self.ingredients = [ingredient_one, ingredient_two]
		self.color = potion_color
		self.sign = potion_sign

	def get_ingredients(self):
		return self.ingredients

	def get_color(self):
		return self.color

	def get_sign(self):
		return self.sign
