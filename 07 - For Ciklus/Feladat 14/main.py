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
    if i % 5 == 0:
        count = count + 1
    elif i % 7 == 0:
        countTwo = countTwo + 1

print(count)
print(countTwo)

if count > countTwo:
    print("Az öttel osztható számok összege nagyobb a héttel osztható számok összegénél!")
elif count == countTwo:
    print("Az öttel osztható számok összege és a héttel osztható számok összege egyenlő!")
else:
    print("A héttel osztható számok összege nagyobb mint az öttel osztható számok összege!")

