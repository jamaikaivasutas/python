from os import *

userNumberInput: int = 0
userMaxNumber: int = 0
userNumberSum: int = 0
inputSum: int = 0


print("Kérem adjon meg egy határértéket!")
userMaxNumber = int(input())

while (userNumberSum < userMaxNumber):
    inputSum = inputSum + 1

    print("Mennyit szeretne hozzáadni az értékéhez?")
    userNumberInput = int(input())

    userNumberSum = userNumberSum + userNumberInput

    print(f"Értéke: {userNumberSum}")

print(f"Önnek {inputSum} bekéréssel sikerült elérni a megadott maximum értéket!")



