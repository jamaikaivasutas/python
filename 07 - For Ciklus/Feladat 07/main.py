from os import *

startingInterval: int = None
endingInterval: int = None

print("Kérem a kezdő intervallum értékét!")
startingInterval = int(input())

print("Kérem a végső intervallum értékét!")
endingInterval = int(input())

system('cls')

for i in range(startingInterval, endingInterval, -1):
    print(i)