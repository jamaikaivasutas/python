from os import *

startInterval : int = None
endInterval : int = None
count : int = 0

print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végső intervallumot!")
endInterval = int(input())

system('cls')

for i in range(startInterval, endInterval, 1):
    if i % 3 == 0 and i % 2 != 0:
        count = count + 1

print(f"Összesen {count} szám van ami páratlan, és osztható hárommal!")

