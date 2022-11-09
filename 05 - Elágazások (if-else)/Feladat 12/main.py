from os import *

number: int = None

system('cls')

print("Kérem a számot!")
number = int(input())

system('cls')

if 10 < number < 20:
    print("A szám 10 és 20 között van!")
elif -20 < number < -10:
    print("A szám -10 és -20 között van!")
else:
    print("A szám se 10 és 20, se -10 és -20 között sincs")