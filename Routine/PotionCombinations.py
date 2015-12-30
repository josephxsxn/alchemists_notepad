from Object.PotionList import PotionList
from Object.Potion import Potion
from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign

from Object.Ingredient import Ingredient
from Object.IngredientProperties import IngredientProperties

class PotionCombinations:
	def distinct_potions_list(potionList):
		dist_potions = []
		dist_potion_hashs = set()

		potionList=potionList.get_potions()
		for potion in potionList:
			if potion.get_hash() not in dist_potion_hashs:
				dist_potions.append(potion)
				dist_potion_hashs.add(potion.get_hash())	
		return dist_potions

	def distinct_hash_list(hashList):
		return None

	#Generates the Potion Chances from 2 ingredients
	#Is dumb and does not know about PotionList creations
	#output list[tuple(Potion, potion_count, total_count, %)]
	def generate_ingredient_potions(ip1, ip2):
		totalCount = 0
		possible_potions = []
		
		#Cross Test all Triplets to see what they make!
		for ip1Triplet in ip1.get_alchemical_options():
			for ip2Triplet in ip2.get_alchemical_options():
				totalCount = totalCount + 1
				for ip1A in ip1Triplet.get_alchemicals():
					for ip2A in ip2Triplet.get_alchemicals():
						alchem_res = PotionCombinations.score_alchemicals(ip1A, ip2A)
						if alchem_res is not None:
							possible_potions.append(Potion(ip1.get_name(), ip2.get_name(), PotionColor(alchem_res[0].value), PotionSign(alchem_res[1].value))) 

		#Count all PotionColor PotionSign combos
		point_counts = {}
		for potion in possible_potions:
				if str(potion.get_color())+str(potion.get_sign()) in point_counts:
					point_counts[str(potion.get_color())+str(potion.get_sign())] = point_counts[str(potion.get_color())+str(potion.get_sign())] + 1
				else:
					point_counts[str(potion.get_color())+str(potion.get_sign())] = 1

		#Generate Report Tuples
		report_tuple_list = []
		report_tuple_list.append(('PotionColorPotionSign','PotionCount','TotalCount','Potion %'))
		for pointKey in point_counts.keys():
			report_tuple_list.append((pointKey, point_counts[pointKey], totalCount, point_counts[pointKey]/totalCount))		
		return report_tuple_list
	
	#searches a potion list for existing results
	def postion_list_search(pl, i1, i2):
		for po in pl.get_potions():
			knownIngredients = po.get_ingredients()
			if i1 in knownIngredients and i2 in knownIngredients: 
				print('###Known Potion###')
				print(po.to_string())
				return True
			else:
				return False
	
	#Takes 2 Alchemicals and sees if they make a Color together
	#Returns the Alchemical Color and Sign 
	def score_alchemicals(alchemical_one, alchemical_two):
		if alchemical_one.get_color() is alchemical_two.get_color():
			if alchemical_one.get_sign() is alchemical_two.get_sign():	
				if alchemical_one.get_size() is not alchemical_two.get_size():
					return (alchemical_one.get_color(), alchemical_two.get_sign())
		else:
			return None	
					
	
