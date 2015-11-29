from Object.Ingredient import Ingredient

from Object.PotionList import PotionList
from Object.PotionFactory import PotionFactory
from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign

from UI.CLIOption import CLIOption
class CLI:
	
	#Statful values for the current game
	ingredient_dic = {}
	potion_list = PotionList()

	def __init__(self):
		print('')
	
	def shell(self):
		print('Select An Option From the Below List')
		for option in CLIOption:
			print(str(option) + ' = ' + str(option.value))
		OPTION = CLIOption(int(input("Enter a Corresponding Number: ")))

		if OPTION is CLIOption.ADD_POTION:
			self.potion_list.add_potion(self.potion_wizard())
			print('Added Potion')
		elif OPTION is CLIOption.LOOKUP_POTION:
			self.lookup_potion()
		elif OPTION is CLIOption.DISTINCT_POTIONS:
			self.distinct_brewed_potions()
		elif OPTION is CLIOption.ESTIMATE_POTIONS:
			self.estimate_potion_combinations()
		elif OPTION is CLIOption.GET_INGREDIENT_ALCHEMICALS:
			self.get_ingredient_alchemicals()

	#potion creation wizard		
	def potion_wizard(self):
		#STDOUT Text Here
		print('Potion Creation Wizard')
		for option in Ingredient:
			print(str(option) + ' = ' + str(option.value))
		i1 = input('Ingredient #1 Number? ')	
		i2 = input('Ingredient #2 Number? ')	
		for option in PotionColor:
			print(str(option) + ' = ' + str(option.value))
		color = input('Potion Color Number? ')
		for option in PotionSign:
			print(str(option) + ' = ' + str(option.value))
		sign = input('Potion Sign Number? ')

		p = PotionFactory.create_potion(Ingredient(int(i1)), Ingredient(int(i2)), PotionColor(int(color)), PotionSign(int(sign)))
		print('Created Potion => ' + p.to_string())
		return p	


	#looksup a potion type from the potion_list, 
	#prints all know valid potion combos
	def lookup_potion(self):
		print('not yet implemented')
		return None

	#List all types of Distinct Potions Ever Brewed
	def distinct_brewed_potions(self):
		print('not yet implemented')
		return None

	#Return % Chances to make PotionType with 2 Ingredients	
	def estimate_potion_combinations(self):
		print('not yet implemented')
		return None

	#return all pottible alchemical combinations for ingredient
	def get_ingredient_alchemicals(self):
		print('not yet implemented')
		return None
