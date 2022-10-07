from os import *

myName : str = None 
birthDate : int = None

print("Kérem adja meg a nevét: ")
myName = str(input())

print("Kérem adja meg a születési évét: ")
birthDate = int(input())

system('cls')

print(f"{myName}, ön {birthDate}-ban született! ")