from os import *

firstNumber: int = None
secondNumber: int = None

system('cls')

print("Kérem az első számot")
firstNumber = int(input())

print("Kérem a második számot")
secondNumber = int(input())

system('cls')

if firstNumber > secondNumber:
    print(f"{firstNumber}")
else:
    print(f"{secondNumber}")