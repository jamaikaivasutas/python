from os import *

firstNumber: int = None
secondNumber:  int = None
solution: int = None

print("Kérem az első számot!")
firstNumber = int(input())

print("Kérem a második számot!")
secondNumber =  int(input())

equation= input("A két számmal milyen műveletet szeretne elvégezni? (+, - , * , / ) ")

match equation:
    case "+":
        solution = firstNumber + secondNumber
        print(f"A megoldás {solution}")
    case "-":
        solution = firstNumber - secondNumber
        print(f"A megoldás {solution}")
    case "*":
        solution = firstNumber * secondNumber
        print(f"A megoldás {solution}")
    case "/":
        solution = firstNumber / secondNumber
        print(f"A megoldás {solution}")