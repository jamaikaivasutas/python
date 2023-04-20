from os import *

userInputNumber: int = None
temp: str = None
isNumber: bool = False
truncatedString: str = None

while userInputNumber == None or userInputNumber > 99 and userInputNumber % 2 != 0:
    print("Kérem adjon meg egy számot! (Maximum kétjegyű lehet)")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if (isNumber) :
        userInputNumber = int(temp) 

    if (userInputNumber > 99):
        print("Max kétjegyű számot adhat meg! Próbálja újra!")


if userInputNumber % 2 != 0:
    userInputNumber = userInputNumber - 1
    
