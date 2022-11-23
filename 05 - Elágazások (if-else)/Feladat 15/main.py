from os import *

vegetableSoup: bool = False
meatSoup: bool = False
fruitSoup: bool = False

chickenThigh: bool = False
chickenBreast: bool = False
vegetableGratin: bool = False
spagetti: bool = False
pizza: bool = False

rice: bool = False
steamedVegetables: bool = False
fruit: bool = False
frenchFries: bool = False
salad: bool = False
cola: bool = False

choice: int = None
secondChoice: int = None
thirdChoice: int = None

isThereAppetizer: bool = False
isThereMainCourse: bool = False
isThereASideDish: bool = False

print("Kérem a menüben szereplő ételeket/köreteket!")
print("Zöldségleves [1]")
print("Húsleves [2]")
print("Gyümölcsleves [3]")

choice = int(input())

if (choice == 1):
    vegetableSoup = True
elif (choice == 2):
    meatSoup = True
elif (choice == 3):
    fruitSoup = True

print("Sültcsirkecomb [1]")
print("Sült csirkemell [2]")
print("Rakottzöldség [3]")
print("Spagetti [4]")
print("Pizza [5]")

secondChoice = int(input())

if (secondChoice == 1):
    chickenThight = True
elif (secondChoice == 2):
    chickenBreast = True
elif (secondChoice == 3):
    vegetableGratin = True
elif (secondChoice == 4):
    spagetti = True
elif (secondChoice == 5):
    pizza = True

print("Rizs [1]")
print("Pároltzöldség [2]")
print("Gyümölcs [3]")
print("Sültkrumpli [4]")
print("Saláta [5]")
print("Kóla [6]")

thirdChoice = int(input())

if (thirdChoice == 1):
    rice = True
elif (thirdChoice == 2):
    steamedVegetables = True
elif (thirdChoice == 3):
    fruit = True
elif (thirdChoice == 4):
    frenchFries = True
elif (thirdChoice == 5):
    salad = True
elif (thirdChoice == 6):
    cola = True

isThereAppetizer = (vegetableSoup or meatSoup or fruitSoup)
isThereMainCourse = (chickenThigh or chickenBreast or vegetableGratin or spagetti or pizza)
isThereASideDish = (rice or steamedVegetables or fruit or frenchFries or salad or cola)
    
if (isThereAppetizer or isThereMainCourse or isThereASideDish):
    if ()
