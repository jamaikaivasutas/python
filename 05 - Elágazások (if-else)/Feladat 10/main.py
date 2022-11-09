from os import *

number: int = None

system('cls')

print("Kérem a számot")
number = int(input())

system('cls')

if number % 2 == 0 and number % 3 == 0:
    print("ZIZI")
elif number % 2 == 0:
    print("BIZ")
elif number % 3 ==0:
    print("BAZ")