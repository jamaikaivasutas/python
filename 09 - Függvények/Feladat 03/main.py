import re
from consoleIO import *

print("Kérem adja meg a nevét: ", end="")
name = str(input())

print("Kérem adja meg születési dátumát: ", end="")
date = str(input())

age = age(date)

print(f"{name}, ön az idén {age} éves")

