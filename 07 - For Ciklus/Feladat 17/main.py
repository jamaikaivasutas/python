from os import *

startInterval : int = None
endInterval : int = None
average: int = None
count : int = 0

print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végső intervallumot!")
endInterval = int(input())

system('cls')

for i in range(startInterval, endInterval, 1):
    count = count + i


average = (count) / 2
print(average)