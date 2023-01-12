from os import *

startInterval : int = None
endInterval : int = None
count : int = 0
countTwo: int = 0
countThree: int = 0


print("Kérem a kezdő intervallumot!")
startInterval = int(input())

print("Kérem a végső intervallumot!")
endInterval = int(input())

system('cls')

for i in range(startInterval, endInterval, 1):
    if i 0:
        countThree = countThree + 1
    elif i % 2 == 0:
        count = count + i
    elif i % 2 != 0:
        countTwo = countTwo + i
   

average = (count + countTwo) / countThree
print(average)


