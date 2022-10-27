from os import *

number: int = None

system('cls')

print("Kérek egy számot!")
number = int(input())

system('cls')

if (number > -30 and number < 40):
    print("A szám -30 és 40 között megtalálható")
else:
    print("A szám nem található meg -30 és 40 között")