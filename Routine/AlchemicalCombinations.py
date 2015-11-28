from Object.Alchemical import Alchemical
from Object.AlchemicalTriplet import AlchemicalTriplet
from Object.AlchemicalColor import AlchemicalColor
from Object.AlchemicalSign import AlchemicalSign
from Object.AlchemicalSize import AlchemicalSize
from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign

class AlchemicalCombinations:
	#Takes a Potion, and Dictonary of IngredientProperties
	#Returns simple potion only  reduction of AlchemicalTriplets for Ingredients used
	def reduce_potion_alchemicals(self, potion, ingredients_prop_dic):
		potion_ingredients = potion.get_ingredients()
		potion_color = potion.get_color()
		potion_sign = potion.get_sign()

		#create all simple conbinations based only off
		#potion results for AlchemicalTriplets
		#if not exist in dic then create all new Triplets
		ingredient_options_list = {}
		if potion_color is not PotionColor.NEUTRAL and potion_sign is not PotionSign.NEUTRAL: 
			for ingredient in potion_ingredients:
				#print(ingredients_prop_dic.keys())
				if ingredient in ingredients_prop_dic:
					#print('IngredientMatched => ' + str(ingredient))
					ingredient_options_list[ingredient]=self.potion_only_filter(ingredients_prop_dic[ingredient].get_alchemical_options(), potion_color, potion_sign)
				else:
					#print('IngredientNOTMatched => ' + str(ingredient))
					ingredient_options_list[ingredient]=self.potion_only_filter(self.inital_alchemical_options(), potion_color, potion_sign)

		else:
			#If it exits return itself
			for ingredient in potion_ingredients:
				#SELF
				if ingredient in ingredients_prop_dic:
					print('SELF => ' + str(ingredient))
					print('Options =>' + str(len(ingredients_prop_dic[ingredient].get_alchemical_options())))
					ingredient_options_list[ingredient] = ingredients_prop_dic[ingredient].get_alchemical_options()
				#ALL
				else:
					print('ALL => ' + str(ingredient))
					ingredient_options_list[ingredient] = self.inital_alchemical_options()

		return ingredient_options_list


	#Filters list of AlchemicalTriplets to acceptalbe Triplets by Input Color & Sign	
	def potion_only_filter(self, triplet_list, color, sign):
		filtered_alchemical_triplets = []
		for triplet in triplet_list:
			for alchem in triplet.get_alchemicals():
				#print('ALCHEM COLOR => ' + str(alchem.get_color().value) + ' ' + str(color.value) + ' SIGN => ' + str(alchem.get_sign().value) + ' ' + str(sign.value))
				if alchem.get_color().value == color.value and alchem.get_sign().value == sign.value:
					#print('MATCHED')
					filtered_alchemical_triplets.append(triplet)
		return filtered_alchemical_triplets



	#Generates all possible AlchemicalTriplets for given Sign and Color of Potion
	#This is used when a Ingredient doesn't exist in our Dictonary yet
	def inital_alchemical_options(self):
		inital_ingredient_triplets = []	
		#RED Alchemical - OUTTER Alchemical in For Loop
		for red_sign in AlchemicalSign:
			#Inital RESET for all Alchemicals after collection
			red_alchemical = None
			blue_alchemical = None
			green_alchemical = None
			for red_size in AlchemicalSize:
				red_alchemical = Alchemical(AlchemicalColor.RED, red_sign, red_size)
				#BLUE Alchemical - MIDDLE Alchemical in For Loop
				for blue_sign in AlchemicalSign:
					for blue_size in AlchemicalSize:
						blue_alchemical = Alchemical(AlchemicalColor.BLUE, blue_sign, blue_size)
						#Green Alchemical - INNER Alchemical in For Loop
						#This is were we collect the Alchemicals into a Triplet
						for green_sign in AlchemicalSign:
							for green_size in AlchemicalSize:
								green_alchemical = Alchemical(AlchemicalColor.GREEN, green_sign, green_size)
								inital_ingredient_triplets.append(AlchemicalTriplet([red_alchemical, blue_alchemical, green_alchemical]))	
	
		return inital_ingredient_triplets
		
