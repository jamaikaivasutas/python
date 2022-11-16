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

print("Kérem a menüben szereplő ételeket/köreteket!")
print("Zöldségleves [1]")
print("Húsleves [2]")
print("Gyümölcsleves [3]")

choice = int(input())

if choice == 1:
    vegetableSoup = True
elif choice == 2:
    meatSoup = True
elif choice == 3:
    fruitSoup = True

print("Sültcsirkecomb [1]")
print("Sült csirkemell [2]")
print("Rakottzöldség [3]")
print("Spagetti [4]")
print("Pizza [5]")

secondChoice = int(input())





