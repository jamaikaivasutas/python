from os import *
import math

firstNumber: int = 0
secondNumber: int = 0
adjustmentAmount: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None
secondTemp: str = None
isNumberTwo: bool = False
truncatedStringTwo: str = None
thirdTemp: str = None
isNumberThree: bool = False
truncatedStringThree: str = None

while (firstNumber >= secondNumber):
    print("Kérem az első számot!")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if (isNumber):
        firstNumber = int(temp) 
    print("Kérem a második számot!")
    secondTemp = input()
    truncatedStringTwo = secondTemp.replace(".","").replace("-","")
    isNumberTwo = truncatedStringTwo.isnumeric()

    if (isNumberTwo):
        secondNumber = int(secondTemp) 
    print("Kérem a lépésközt!")
    adjustmentAmount = int(input())
    thirdTemp = input()
    truncatedStringThree = thirdTemp.replace(".","").replace("-","")
    isNumberThree = truncatedStringThree.isnumeric()

    if (isNumberThree):
        adjustmentAmount = int(thirdTemp) 

    if firstNumber >= secondNumber:
        print("A második számnak nagyobbnak kell lennie az elsőnél! Kérem próbálja újra!")
  
    

for i in range(secondNumber, firstNumber,  -abs(adjustmentAmount)):
    print(i)
