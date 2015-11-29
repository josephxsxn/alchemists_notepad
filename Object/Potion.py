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

	def to_string(self):
		return 'Potion constructs: ' + str(self.get_ingredients()[0]) + ' ' + str(self.get_ingredients()[1]) + ' ' + str(self.get_color()) + ' ' + str(self.get_sign())

	def get_hash(self):
		return  str(self.get_ingredients()[0].value) + str(self.get_ingredients()[1].value) + str(self.get_color().value) + str(self.get_sign().value)
