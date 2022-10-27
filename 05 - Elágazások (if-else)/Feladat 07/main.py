from os import *

number: int = None

system('cls')

print("Kérem a számot")
number = int(input())

system('cls')

if number % 5 == 0:
    print("A szám osztható öttel")
else:
    print("A szám NEM osztható öttel")