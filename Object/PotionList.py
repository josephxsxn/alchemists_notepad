from Object.Potion import Potion
class PotionList:
	createdPotions = []

	def add_potion(self, potion):
		self.createdPotions.append(potion)

	def get_potions(self):
		return self.createdPotions
	
	def get_potion(self, number):
		try:
			return self.createdPotions[number]
		except IndexError:
			return None
