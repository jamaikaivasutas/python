from os import *

startInterval : int = None
endInterval : int = None
addition: int = 0
multiply: int = 1

print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végső intervallumot!")
endInterval = int(input())

system('cls')

if startInterval % 2 == 0:
    for i in range(startInterval, endInterval, 2):
        addition = addition + i
    for i in range(startInterval + 1, endInterval, 2):
        multiply = multiply * i
else:
    for i in range(startInterval + 1, endInterval, 2):
        addition = addition + i
    for i in range(startInterval, endInterval, 2):
        multiply = multiply * i

print(addition)
print(multiply)