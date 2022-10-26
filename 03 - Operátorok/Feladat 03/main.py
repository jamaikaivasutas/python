from os import *

firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None
solution: int = None

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber = int(input())

print("Kérem a harmadik számot!")
thirdNumber = int(input())

solution: int = (firstNumber - secondNumber) * thirdNumber

system('cls')

print(f"A {firstNumber} és a {secondNumber} különbségének a {thirdNumber} szorosa/szerese {solution}-val/vel egyenlő")