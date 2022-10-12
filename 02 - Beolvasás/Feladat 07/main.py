from os import *

brandName : str = None
modelName : str = None
type : str = None
cubicCentimeters : int = None
releaseDate : int = None

print("Kérem a kedvenc autómárkájának nevét!",end="")
brandName = str(input())

print(f"Kérem a {brandName} autómárkából a kedvenc autójának a modelljét!",end="")
modelName = str(input())

print(f"Kérem a {brandName} márkájú {modelName} modellű autójának kedvenc típusát!",end="")
type = str(input())

print(f"a {brandName} {modelName} {type} autó hány köbcenti?",end="")
cubicCentimeters = int(input())

print(f" A {brandName} {modelName} {type} autó melyik évben jelent meg?",end="")
releaseDate = int(input())

system('cls')

print(f"Márka: {brandName}\nModell: {modelName}\nTípus: {type}\nKöbcenti: {cubicCentimeters}\nMegjelenési év: {releaseDate}")




