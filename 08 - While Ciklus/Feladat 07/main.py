from os import *
import math

firstNumber: int = 0
secondNumber: int = 0
adjustmentAmount: int = 0

while (firstNumber >= secondNumber):
    print("Kérem az első számot!")
    firstNumber = int(input())
    print("Kérem a második számot!")
    secondNumber = int(input())
    print("Kérem a lépésközt!")
    adjustmentAmount = int(input())

    if firstNumber >= secondNumber:
        print("A második számnak nagyobbnak kell lennie az elsőnél! Kérem próbálja újra!")
  
    

for i in range(secondNumber, firstNumber,  -abs(adjustmentAmount)):
    print(i)
