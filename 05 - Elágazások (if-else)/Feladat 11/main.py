from os import *

number: int = None

system('cls')

print("Kérem a számot!")
number = int(input())

system('cls')

if 0 < number and number % 2 == 0 and number % 5 == 0:
    print("A szám pozitív, páros, és osztható 5-el.")
elif 0 < number and number % 2 == 0 and number % 5 != 0:
    print("A szám pozitív, páros, de nem osztható öttel")
elif 0 < number and number % 2 != 0 and number % 5 == 0:
    print("A szám pozitív, páratlan, és osztható öttel.")
elif 0 < number and number % 2 != 0 and number % 5 != 0: 
    print("A szám pozitív, páratlan, és nem osztható öttel")
