from Object.PotionList import PotionList
from UI.CLIOption import CLIOption
class CLI:
	
	#Statful values for the current game
	ingredient_dic = {}
	potion_list = PotionList()

	def __init__(self):
		print('constructor')
	
	def shell(self):
		print('Select An Option From the Below List')
		for option in CLIOption:
			print(str(option) + ' = ' + str(option.value))	
		OPTION = input("Enter a Corresponding Number: ")
				

	#insert a potion into the potion list		
	def add_potion(self):
		return None
	
	#looksup a potion type from the potion_list, 
	#prints all know valid potion combos
	def lookup_potion(self):
		return None

	#Builts Potions Objects in CLI Walkthrew
	def make_potion_helper(self):
		return None

	#List all types of Distinct Potions Ever Brewed
	def distinct_brewed_potions(self):
		return None

	#Return % Chances to make PotionType with 2 Ingredients	
	def estimate_potion_cobminations(self, ingredient1, ingredient2):
		return None

	#return all pottible alchemical combinations for ingredient
	def get_ingredient_alchemicals(self, ingredient):
		return None
