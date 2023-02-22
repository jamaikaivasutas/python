from os import *

userAgeInput: int = None
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (userAgeInput == None or userAgeInput < 0 or userAgeInput > 99):
    print("Kérem adja meg az életkorát!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if (isNumber) :
        userAgeInput = int(temp) 
    
    if 0 <= userAgeInput <= 6:
        print("Gyerek")
    elif 7 <= userAgeInput <= 18:
        print("Iskolás")
    elif 19 <= userAgeInput <= 65:
        print("Dolgozó")
    elif userAgeInput > 65:
        print("Nyugdíjas")