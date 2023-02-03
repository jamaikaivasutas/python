from os import *
import random

randomNumber = random.randint(1,9)
userGuess: int = 0
count: int = 0

while (userGuess != randomNumber and count < 5):
    count = count + 1
    print("Találja ki a számot!")
    userGuess = int(input())
    if userGuess == randomNumber:
        print("Sikeresen kitalálta a számot!")
    else:
        print("Sajnos nem sikerült, próbálja újra")

