class IngredientProperties:
	alchemical_options = []

	def __init__(self, ingredient_name):
		self.ingredient_name = ingredient_name
	
	def get_name(self):
		return self.ingredient_name

	def get_alchemical_options(self):
		return self.alchemical_options

	def set_alchemical_options(self, alchemical_list):
		self.alchemical_options = alchemical_list
