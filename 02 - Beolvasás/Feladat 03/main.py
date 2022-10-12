from os import * 

myName : str = None
myHeight: float = None

print("Kérem az ön nevét: ",end="")
myName = str(input())

print("Kérem az ön magasságát méterben: ",end="")
myHeight = float(input())

system('cls')

print(f"{myName} az ön magassága {myHeight}m!")