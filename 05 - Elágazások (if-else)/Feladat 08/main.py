from os import *

number: int = None

system('cls')

print("Kérem a számot!")
number = int(input())

system('cls')

if (number % 4 == 0 and number % 6 == 0):
    print("A szám oszható 6-al és 4-el is!")
elif (number % 4 == 0 and number % 6 != 0):
    print("A szám osztható 4-el, de 6-al nem.")
elif (number % 4 != 0 and number % 6 == 0):
    print("A szám osztható 6-al, de 4-el nem.")
else:
    print("A szám nem osztható 4-el se és 6-al se")