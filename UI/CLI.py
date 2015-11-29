from Object.Ingredient import Ingredient
from Object.IngredientProperties import IngredientProperties
from Object.PotionList import PotionList
from Object.PotionFactory import PotionFactory
from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign

from Routine.AlchemicalCombinations import AlchemicalCombinations
from Routine.PotionCombinations import PotionCombinations

from UI.CLIOption import CLIOption

import sys

class CLI:
	
	#Statful values for the current game
	ingredient_dic = {}
	potion_list = PotionList()


	def __init__(self):
		print('')
	
	def shell(self):
		print('Select An Option From the Below List')
		while(True):
			for option in CLIOption:
				print(str(option) + ' = ' + str(option.value))
			OPTION = CLIOption(int(input("Enter a Corresponding Number: ")))

			if OPTION is CLIOption.ADD_POTION:
				p = self.potion_wizard()
				self.potion_list.add_potion(p)
				self.update_ingredient_dic(p)
				print('Added Potion to PotionList')
			elif OPTION is CLIOption.LOOKUP_POTION:
				potion_combos = self.lookup_potion()
				for potion in potion_combos:
					print(str(potion.get_color()) + ' ' + str(potion.get_sign()) + ' ' + str(potion.get_ingredients()[0]) + ' ' + str(potion.get_ingredients()[1]))	
			elif OPTION is CLIOption.DISTINCT_POTIONS:
				self.distinct_brewed_potions()
			elif OPTION is CLIOption.ESTIMATE_POTIONS:
				self.estimate_potion_combinations()
			elif OPTION is CLIOption.GET_INGREDIENT_ALCHEMICALS:
				count = 0
				for triplet in self.get_ingredient_alchemicals():
					flavorText = '###Triplet#'+str(count)+'###'
					for a in triplet.get_alchemicals():
		 				print(flavorText+ ' ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))
					count = count + 1	
				
			elif OPTION is CLIOption.QUIT:
				sys.exit(0)

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
		for option in PotionColor:
			print(str(option) + ' = ' + str(option.value))
		color = input('Potion Color Number? ')
		for option in PotionSign:
			print(str(option) + ' = ' + str(option.value))
		sign = input('Potion Sign Number? ')
		print('Looking up Combos for: ' + str(PotionColor(int(color))) + ' ' + str(PotionSign(int(sign))))
		matching = []
		for potion in self.potion_list.get_potions():
			if potion.get_color() is PotionColor(int(color)) and potion.get_sign() is PotionSign(int(sign)):
				matching.append(potion)
		return matching 
			

	#List all types of Distinct Potions Ever Brewed
	def distinct_brewed_potions(self):
		for potion in PotionCombinations.distinct_potions_list(self.potion_list):	
			print(str(potion.to_string() + ' #' + potion.get_hash()))

	#Return % Chances to make PotionType's with 2 Ingredients	
	def estimate_potion_combinations(self):
		print('not yet implemented')

	#return all pottible alchemical combinations for ingredient
	def get_ingredient_alchemicals(self):
		for option in Ingredient:
			print(str(option) + ' = ' + str(option.value))
		i1 = input('Ingredient Number? ')
		return self.ingredient_dic[Ingredient(int(i1))].get_alchemical_options()	

	#Update Ingredient Dic with PotionResults
	def update_ingredient_dic(self, potion):
		reduction = AlchemicalCombinations().reduce_potion_alchemicals(potion, self.ingredient_dic)
		for ingredient in potion.get_ingredients():
			#build new IP for each
			if ingredient in self.ingredient_dic:
				ip = self.ingredient_dic[ingredient]
				ip.set_alchemical_options(reduction[ingredient])
			else:
				ip = IngredientProperties(ingredient)
				ip.set_alchemical_options(reduction[ingredient])
			self.ingredient_dic[ingredient] = ip
					
