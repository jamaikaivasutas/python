from os import *

whatDay = input("Hányadik napja van a hétnek? ")

match whatDay:
    case "1":
        print("Hétfő van")
    case "2": 
        print("Kedd van")
    case "3":
        print("Szerda van")
    case "4":
        print("Csütörtök van")
    case "5":
        print("Péntek van")
    case "6":
        print("Szombat van")
    case "7":
        print("Vasárnap van")
    case _:
        print("Egy hét csak 7 napból áll, ilyen nap nincsen.")