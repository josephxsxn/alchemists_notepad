#List all ENUMS 
from Object.Ingredient import Ingredient
for i in Ingredient:
	print(i)

from Object.PotionColor import PotionColor
for r in PotionColor:
	print(r)

from Object.PotionSign import PotionSign
for r in PotionSign:
	print(r)
#//TODO
#NEED TO ADD ALCHEMICAL ENUMS HERE

#Make a Potion and Fetch its values
from Object.Potion import Potion
from Object.PotionColor import PotionColor
from Object.PotionSign import PotionSign
flowertoad = Potion(Ingredient.TOAD, Ingredient.FLOWER, PotionColor.RED, PotionSign.POSITIVE)
print(flowertoad.get_ingredients())
print(flowertoad.get_color())
print(flowertoad.get_sign())

###Put some Potions in the List and Get back
from Object.PotionList import PotionList
polist = PotionList()
polist.add_potion(flowertoad)
pores = polist.get_potions()
for po in pores:
	print(po.get_ingredients())
	print(po.get_color())
	print(po.get_sign())

#Get an exact one from the list
pores = polist.get_potion(0)
print(pores.get_ingredients())
print(pores.get_color())
print(pores.get_sign())

#fetch one that doesnt exist from the list
pores = polist.get_potion(1)
print(pores)

#make an few Alchemicals
from Object.Alchemical import Alchemical
from Object.AlchemicalColor import AlchemicalColor
from Object.AlchemicalSign import AlchemicalSign
from Object.AlchemicalSize import AlchemicalSize
#triplet one
redposlarge = Alchemical(AlchemicalColor.RED, AlchemicalSign.POSITIVE, AlchemicalSize.LARGE)
bluenegsmall = Alchemical(AlchemicalColor.BLUE, AlchemicalSign.NEGATIVE, AlchemicalSize.SMALL)
greennegsmall = Alchemical(AlchemicalColor.GREEN, AlchemicalSign.NEGATIVE, AlchemicalSize.SMALL)

#triplet two
redpossmall = Alchemical(AlchemicalColor.RED, AlchemicalSign.POSITIVE, AlchemicalSize.SMALL)
bluepossmall = Alchemical(AlchemicalColor.BLUE, AlchemicalSign.POSITIVE, AlchemicalSize.SMALL)
greenposlarge = Alchemical(AlchemicalColor.GREEN, AlchemicalSign.POSITIVE, AlchemicalSize.SMALL)

print('T1 ' + str(redposlarge.get_color()) + ' ' + str(redposlarge.get_sign()) + ' ' + str(redposlarge.get_size()))
print('T1 ' + str(bluenegsmall.get_color()) + ' ' + str(bluenegsmall.get_sign()) + ' ' + str(bluenegsmall.get_size()))
print('T1 ' + str(greennegsmall.get_color()) + ' ' + str(greennegsmall.get_sign()) + ' ' + str(greennegsmall.get_size()))

print('T2 ' + str(redpossmall.get_color()) + ' ' + str(redpossmall.get_sign()) + ' ' + str(redpossmall.get_size()))
print('T2 ' + str(bluepossmall.get_color()) + ' ' + str(bluepossmall.get_sign()) + ' ' + str(bluepossmall.get_size()))
print('T2 ' + str(greenposlarge.get_color()) + ' ' + str(greenposlarge.get_sign()) + ' ' + str(greenposlarge.get_size()))

#make a Triplet
from Object.AlchemicalTriplet import AlchemicalTriplet
triplet_one = AlchemicalTriplet([redposlarge, bluenegsmall, greennegsmall])
triplet_one_list = triplet_one.get_alchemicals()
for a in triplet_one_list:
	print('Triplet_ONE ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))

triplet_two = AlchemicalTriplet([redpossmall, bluepossmall, greenposlarge])
triplet_two_list = triplet_two.get_alchemicals()
print(triplet_two_list)
for b in triplet_two_list:
	print('Triplet_TWO ' + str(b.get_color()) + ' ' + str(b.get_sign()) + ' ' + str(b.get_size()))
#make some ingredients and properties
from Object.IngredientProperties import IngredientProperties
ip = IngredientProperties(Ingredient.TOAD)
print(str(ip.get_name()))
print(ip.get_alchemical_options())
ip.set_alchemical_options([triplet_one])
ip_triplet_list = ip.get_alchemical_options()

#for given ingredient list all triplet props
for l in ip_triplet_list:
	for a in l.get_alchemicals():
		print('IngredientProps ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))

#Alchemical Combinations Test
from Routine.AlchemicalCombinations import AlchemicalCombinations
ingredient_dic = {Ingredient.TOAD : ip}
print(ingredient_dic.keys())
triplet_list = ingredient_dic[Ingredient.TOAD].get_alchemical_options()
for triplet in triplet_list:
	for a in triplet.get_alchemicals():
		 print('AC Combos ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))
ac = AlchemicalCombinations()
res = ac.reduce_potion_alchemicals(polist.get_potion(0), ingredient_dic)
print(polist.get_potion(0).get_ingredients())
print(polist.get_potion(0).get_sign())
print(polist.get_potion(0).get_color())
print(res.keys())
triplet_list = res[Ingredient.TOAD]
for triplet in triplet_list:
	for a in triplet.get_alchemicals():
		 print('Filtered Toad Combos ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))
print(len(res[Ingredient.TOAD]))
print(len(res[Ingredient.FLOWER]))
#triplet_list = res[Ingredient.FLOWER]
#for triplet in triplet_list:
#	for a in triplet.get_alchemicals():
#		 print('Filtered Flower Combos ' + str(a.get_color()) + ' ' + str(a.get_sign()) + ' ' + str(a.get_size()))

ip = IngredientProperties(Ingredient.FLOWER)
print(str(ip.get_name()))
print(ip.get_alchemical_options())
ip.set_alchemical_options(res[Ingredient.FLOWER])
ingredient_dic[Ingredient.FLOWER] = ip

print('TOAD LEN ' + str(len(ingredient_dic[Ingredient.TOAD].get_alchemical_options())))
print('FLOWER LEN ' + str(len(ingredient_dic[Ingredient.FLOWER].get_alchemical_options())))


initalTriplets = ac.inital_alchemical_options()
print(len(initalTriplets))
print(len(ac.potion_only_filter(initalTriplets, polist.get_potion(0).get_color(), polist.get_potion(0).get_sign())))

#################
###NEUTRAL POTION
#################
herbtoad = Potion(Ingredient.TOAD, Ingredient.HERB, PotionColor.NEUTRAL, PotionSign.NEUTRAL)
polist.add_potion(herbtoad)
#ac2 = AlchemicalCombinations()

res = ac.reduce_potion_alchemicals(herbtoad, ingredient_dic)
print(polist.get_potion(1).get_ingredients())
print(polist.get_potion(1).get_sign())
print(polist.get_potion(1).get_color())
print(res.keys())
print('TOAD LEN RES: ' + str(len(res[Ingredient.TOAD])))
print('HERB LEN RES: ' + str(len(res[Ingredient.HERB])))
ip = IngredientProperties(Ingredient.TOAD)
print(str(ip.get_name()))
ip.set_alchemical_options(res[Ingredient.TOAD])
ingredient_dic[Ingredient.TOAD] = ip

ip = IngredientProperties(Ingredient.HERB)
print(str(ip.get_name()))
ip.set_alchemical_options(res[Ingredient.HERB])
ingredient_dic[Ingredient.HERB] = ip
print(ingredient_dic.keys())

