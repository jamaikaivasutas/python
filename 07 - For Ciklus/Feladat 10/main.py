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

if (endInterval > startInterval):
    for i in range(startInterval, endInterval, 1):
        print(i)
    
    addition = addition + i
    multiply = multiply*i
    print(addition)
    print(multiply) 
else:
    for i in range(startInterval,endInterval, -1):
        print(i)
    addition = addition + i
    multiply = multiply* i
    print(addition)
    print(multiply)