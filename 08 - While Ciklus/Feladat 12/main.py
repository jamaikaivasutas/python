from os import *

userMoneyOriginal: int = 0
count: int = 0

print("Mennyi pénze van önnek?")
userMoneyOriginal = int(input())

userMoney = userMoneyOriginal

while userMoney < 100000:
    count = count + 1

    userMoney = userMoney + (userMoneyOriginal * 0.02)


print(f"Az ön pénze {count} hónap múlva éri el a 100.000 Ft-ot a bankban!")
