from os import *

startInterval: int = None
endInterval: int = None

print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végző intervallumot!")
endInterval = int(input())

system('cls')

if startInterval % 2 == 0:
    startInterval = startInterval + 1
    for i in range(startInterval, endInterval, 2):
        print(i)
else:
    for i in range(startInterval, endInterval,):
        print(i)