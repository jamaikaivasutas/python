from os import *

number: int = None

print("Kérek egy számot!")
number = int(input())

system('cls')

if number > 0:
    print("A szám nagyobb mint 0")
elif number == 0:
    print("A szám 0!")
else:
    print("A szám kisebb mint nulla")