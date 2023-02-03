from os import *

userAgeInput: int = None

while (userAgeInput == None or userAgeInput < 0 or userAgeInput > 99):
    print("Kérem adja meg az életkorát!")
    userAgeInput = int(input())
    if 0 <= userAgeInput <= 6:
        print("Gyerek")
    elif 7 <= userAgeInput <= 18:
        print("Iskolás")
    elif 19 <= userAgeInput <= 65:
        print("Dolgozó")
    elif userAgeInput > 65:
        print("Nyugdíjas")