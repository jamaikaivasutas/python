from os import *

number: int = None

system('cls')

print("Kérem a számot!")
number = int(input())

system('cls')

if 0 <= number <= 9:
    print("Egyjegyű szám")
elif 10 <= number <= 99:
    print("Kétjegyű szám")
elif 100 <= number <= 999:
    print("Háromjegyű szám")