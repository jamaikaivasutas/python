from os import *

firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
fourthNumber: int = None
solution: float = None

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber = int(input())

print("Kérem a harmadik számot!")
thirdNumber = int(input())

print("Kérem a negyedik számot!")
fourthNumber = int(input())

solution: float = (firstNumber + secondNumber) / (thirdNumber - fourthNumber)

system('cls')

print(f"A {firstNumber} és a {secondNumber} összegének és a {thirdNumber} és a {fourthNumber} különbségének a hányadosa {solution}")

