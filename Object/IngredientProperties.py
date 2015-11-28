class IngredientProperties:
	def __init__(self, ingredient_name):
		self.ingredient_name = ingredient_name
		self.alchemical_options = []
	
	def get_name(self):
		return self.ingredient_name

	def get_alchemical_options(self):
		return self.alchemical_options

	def set_alchemical_options(self, alchemical_list):
		self.alchemical_options = alchemical_list
