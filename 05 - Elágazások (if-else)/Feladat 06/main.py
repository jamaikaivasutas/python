from os import *

firstNumber: int = None
secondNumber: int = None
thirdNumber: int = None

system('cls')

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber = int(input())

print("Kérem a harmadik számot!")
thirdNumber = int(input())

system('cls')

if firstNumber < secondNumber < thirdNumber:
    print(f"{firstNumber}, {secondNumber}, {thirdNumber}")
elif firstNumber < thirdNumber < secondNumber:
    print(f"{firstNumber}, {thirdNumber}, {secondNumber}")
elif secondNumber < firstNumber < thirdNumber:
    print(f"{secondNumber}, {firstNumber}, {thirdNumber}")
elif secondNumber < thirdNumber < firstNumber:
    print(f"{secondNumber}, {thirdNumber}, {firstNumber}")
elif thirdNumber < firstNumber < secondNumber: 
    print(f"{thirdNumber}, {firstNumber}, {secondNumber}")
elif thirdNumber < secondNumber < firstNumber: 
    print(f"{thirdNumber} , {secondNumber} , {firstNumber}")
