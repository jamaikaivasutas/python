from consoleIO import *
from stringFunctions import *

firstWord: str = readWordFromConsole()
secondWord: str = readWordFromConsole()

commonLetters: int = searchCommonLetters(firstWord, secondWord)

print(commonLetters)