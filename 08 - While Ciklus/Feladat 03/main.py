from os import *
import random

randomNumber = random.randint(1,9)
userGuess: int = 0
count: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (userGuess != randomNumber and count < 5):
    count = count + 1
    print("Találja ki a számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()
    if (isNumber):
        userGuess = int(temp)

   


if (userGuess == randomNumber):
    print("Sikeresen kitalálta a számot!")
else:
    print("Sajnos nem sikerült, próbálja újra")
    if (count >= 5):
        print("Elérte az 5 próbálkozást, nem próbálkozhat többször!")