from os import *

firstNumber: int = None
secondNumber: int = None

system('cls')

print("Kérem az x-et!")
firstNumber = int(input())

print("Kérem az y-t")
secondNumber = int(input())

system('cls')

if firstNumber % secondNumber == 0:
    print("Az Y osztója az X-nek!")
else:
    print("Az Y NEM osztója az X-nek")