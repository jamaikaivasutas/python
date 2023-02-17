from os import *

oddNumber: int = 0
evenNumber: int = 0

while evenNumber % 2 != 0:
    print("Kérem írjon be egy páros számot!")
    evenNumber = int(input())

while oddNumber < evenNumber or oddNumber % 2 == 0:
    print("Kérem írjon be az előző számnál nagyobb páratlan számot!")