from os import *

firstNumber: int = None
secondNumber: int = None
solution: int = None

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber = int(input())

solution: int = firstNumber + secondNumber

system('cls')

print(f"A {firstNumber} és a {secondNumber} összege {solution}")