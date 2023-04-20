from os import *
from mathfunctions import *
from consoleIO import *

x: float = None
y: float = None
sumResult: float = None
extractionResult: float = None
multiplyResult: float = None
divisionResult: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

sumResult = sumOfTwoNumbers(x,y)
printToConsole(x, y, sumResult, "+")

extractionResult = extractionOfTwoNumbers(x,y)
printToConsole(x, y, extractionResult,  "-")

multiplyResult = multiplicationOfTwoNumbers(x,y)
printToConsole(x, y, multiplyResult, "*")

divisionResult = divisionOfTwoNumbers(x,y)
printToConsole(x, y, divisionResult, "/")

