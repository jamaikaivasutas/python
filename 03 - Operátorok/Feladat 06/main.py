from os import *

firstNumber: float = None
secondNumber: float = None
thirdNumber: int = None
solution: float = None

print("Kérem az első számot!")
firstNumber = float(input())

print("Kérem a második számot!")
secondNumber = float(input())

print("Kérem a harmadik számot!")
thirdNumber = int(input())

solution: float = ((firstNumber + 0.5) * (secondNumber - 0.7)) % thirdNumber

system('cls')

print(f"A {firstNumber} + 0.5 és a {secondNumber} -0.7 elosztva {thirdNumber}-val/vel {solution} maradékot eredményez")