from os import *

firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
solution: float = None

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber = int(input())

print("Kérem a harmadik számot!")
thirdNumber = int(input())

solution: float = (firstNumber * secondNumber) / thirdNumber

system('cls')

print(f"A {firstNumber} és a {secondNumber} szorzatát ha {thirdNumber}-el elosztjuk, akkor {solution} az eredmény")