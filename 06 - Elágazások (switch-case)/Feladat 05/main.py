from os import *

resistor1: int = None
resistor2: int = None

print("Kérem az első ellenállást!")
resistor1 = int(input())

print("Kérem a második ellenállást!")
resistor2 = int(input())

serial: int = None
parallel: int = None

solution = input("Hogyan van kapcsolva az áramköre? \n  Párhuzamosan [p,P]  \n Sorosan [s,S] \n ")

match solution:
    case "P" | "p":
        parallel = (resistor1 + resistor2) / (resistor1 * resistor2)
        print(f"A két ellenállás eredő ellenállása {parallel} ohm")
    case "S" | "s":
        serial = resistor1 + resistor2 
        print(f"A két ellenállás eredő ellenállása {serial} ohm")
    