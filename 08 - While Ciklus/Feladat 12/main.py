from os import *

userMoneyOriginal: int = 0
count: int = 0
userMoney: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None

print("Mennyi pénze van önnek?")
temp = input()
truncatedString = temp.replace(".","").replace("-","")
isNumber = truncatedString.isnumeric()

if (isNumber) :
    userMoneyOriginal = float(temp) 

userMoney = userMoneyOriginal

while userMoney < 100000:
    count = count + 1

    userMoney = userMoney + (userMoneyOriginal * 0.02)


print(f"Az ön pénze {count} hónap múlva éri el a 100.000 Ft-ot a bankban!")
