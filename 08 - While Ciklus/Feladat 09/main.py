from os import *

userNumberInput: int = 0

while userNumberInput <= 99:
    print("Kérem adjon meg egy háromjegyű számot!")
    userNumberInput = int(input())

    if userNumberInput <= 99:
        print("A szám amit megadott nem háromjegyű! Próbálkozzon újra!")

if userNumberInput % 7 == 0:
    print("A szám osztható 7-el!")
else: 
    print("A szám nem osztható 7-el!")       