from os import *

myName : str = None
pressedButton: str = None

print("Kérem az ön nevét: ",end="")
myName = str(input())

print("Nyomjon meg egy gombot a billentyűzetén",end="")
pressedButton = str(input())

system('cls')

print(f"{myName} ön a {pressedButton} gombot nyomta meg!")