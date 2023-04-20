from consoleIO import *
from mathFunctions import *

name:str=None
birthDate:int=None
date:int=None
age:int=None

name:str=readNameFromConsole()
birthDate:int=readAgeFromConsole()
date:int=readDateFromConsole()

age:int=agecalc(birthDate, date)
printWelcomingMessage(name,age)