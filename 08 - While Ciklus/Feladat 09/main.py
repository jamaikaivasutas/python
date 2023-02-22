from os import *

userNumberInput: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (userNumberInput <= 99):
    print("Kérem adjon meg egy háromjegyű számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if (isNumber) :
        userNumberInput = int(temp) 

    if userNumberInput <= 99:
        print("A szám amit megadott nem háromjegyű! Próbálkozzon újra!")

if userNumberInput % 7 == 0:
    print("A szám osztható 7-el!")
else: 
    print("A szám nem osztható 7-el!")       