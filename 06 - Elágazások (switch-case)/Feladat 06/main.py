from os import *
import math

length: int = None
width: int = None
print("Kérem a téglalap hosszát!")
length = int(input())

print("Kérem a téglalap szélességét!")
width = int(input())
solution: int = None
choice = input("Melyiket szeretné kiszámítani? \n terület [t] \n kerület [k] \n átló [a] \n ")

match choice:
    case "k" :
        solution = 2 * (length + width)
        print(f"A téglalap kerülete {solution}")
    case "t" :
        solution = length * width
        print(f"A téglalap területe {solution}")
    case "a" :
        solution = math.sqrt(math.pow(length , 2) + math.pow(width , 2))
        print(f"A téglalap átlója {solution}")