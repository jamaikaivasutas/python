from os import *

yourName: str = None

while yourName == None or len(yourName) <= 2:
    print("Kérem adja meg a nevét!")
    yourName = str(input())
    if len(yourName) <= 2:
        print("A neve kettő karakternél több legyen!")
    else: 
        print(f"Üdvözlöm önt, {yourName}")

