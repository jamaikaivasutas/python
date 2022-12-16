from os import *

startInterval : int = None
endInterval : int = None
count : int = 0
countTwo: int = 0

print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végső intervallumot!")
endInterval = int(input())

system('cls')

for i in range(startInterval, endInterval, 1):
    if i % 2 == 0:
        count = count + 1
    else:
        countTwo = countTwo + 1

print(count)
print(countTwo)

if count > countTwo:
    print("A páros számok összege a nagyobb!")
elif count == countTwo:
    print("A páros és a páratlan számok összege egyenlő!")
else:
    print("A páratlan számok összege a nagyobb!")
