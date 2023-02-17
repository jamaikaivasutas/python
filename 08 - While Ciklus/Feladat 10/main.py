from os import *

userInputNumber: int = 0

while userInputNumber > 99:
    print("Kérem adjon meg egy számot! (Maximum kétjegyű lehet)")
    userInputNumber = int(input())


if userInputNumber % 2 != 0:
    userInputNumber = userInputNumber - 1
    
