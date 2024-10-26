#lists

healtyFoods = ["avocado", "apple"]
#lists are dinamic in python

print("chicken" in healtyFoods)
\
#if statement
if "apple" in healtyFoods:
    print("eat it!")

if "carrot" not in healtyFoods:
    print("buy some!")

backpack = ["pizza", "avocado", "chips", "apple"]

#backpack.remove("avocado")
#print(backpack)

if "pizza" not in healtyFoods:
    backpack.remove("pizza")

if "apple" not in healtyFoods:
    backpack.remove("apple")

print(backpack)

#remove more items from a list
backpack = [item for item in backpack if item in healtyFoods]
