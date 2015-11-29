from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign
from Object.Potion import Potion

class PotionFactory:
	def create_potion(ingredient1, ingredient2, potionColor, potionSign):
		return Potion(ingredient1, ingredient2, potionColor, potionSign)	
