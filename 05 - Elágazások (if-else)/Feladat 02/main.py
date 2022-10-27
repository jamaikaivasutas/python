from os import *

number: int = None

system('cls')

print("Kérek egy számot!")
number = int(input())

system('cls')

if number >= 0:
    print("pozitív")
else:
    print("negatív")