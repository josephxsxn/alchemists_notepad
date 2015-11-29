from Object.PotionList import PotionList
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

	
