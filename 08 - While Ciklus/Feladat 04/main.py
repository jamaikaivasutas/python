from os import *

userNumberInput: int = 0
userInputSum: int = 0
inputCount: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (userInputSum <= 100):
    inputCount = inputCount + 1
    print("Kérem adjon meg egy számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()
    if (isNumber):
        userNumberInput = int(temp)

    userInputSum = userInputSum + userNumberInput

    print(f"Bevitelek száma: {inputCount}")
    print(f"Bevitt számok összege: {userInputSum}")

