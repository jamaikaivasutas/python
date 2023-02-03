from os import *

userNumberInput: int = 0
userInputSum: int = 0
inputCount: int = 0


while (userInputSum <= 100):
    inputCount = inputCount + 1

    print("Kérem adjon meg egy számot!")
    userNumberInput= int(input())

    userInputSum = userInputSum + userNumberInput

    print(f"Bevitelek száma: {inputCount}")
    print(f"Bevitt számok összege: {userInputSum}")

