from os import *

number: int = None

system('cls')

print("Kérem a számot!")
number = int(input())

system('cls')

if (0 < number):
    print("A szám pozitív")
else:
    print("A szám negatív")

if (number % 2) == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

if (number % 5) == 0:
    print("A szám oszható öttel.")
else:
    print("A szám nem osztható öttel.")