from consoleIO import *
from mathFunctions import *

celTemp: int = getTempFromConsole()
tempChoice: str = getTempTypeFromConsole()
tempConverted: int = convertCelsToOther(celTemp, tempChoice)

print(tempConverted)

