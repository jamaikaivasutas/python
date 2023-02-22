from os import *

userSodaInput: int = 0
temp: str = None
isNumber: bool = False
truncatedString: str = None

while (0 >= userSodaInput or userSodaInput > 5):
    print("Válasszon egy üdítőt! \n [1] Coca Cola \n [2] Fanta \n [3] Sprite \n [4] Mountain Dew \n [5] Szentkirályi Ásványvíz (mentes)")
    temp = input()
    truncatedString = temp.replace(".","").replace("-","")
    isNumber = truncatedString.isnumeric()

    if (isNumber) :
        userSodaInput = float(temp) 
    if (0 >= userSodaInput or userSodaInput > 5):
        print("Ilyen üdítő nincs a kínálatunkban, kérem próbálja újra!")
    elif (userSodaInput == 1):
        print("Ön a Coca Colát választotta!")
    elif (userSodaInput == 2):
        print("Ön a Fantát választotta!")
    elif (userSodaInput == 3):
        print("Ön a Spriteot választotta!")
    elif (userSodaInput == 4):
        print("Ön a Mountain Dew-t választotta!")
    elif (userSodaInput == 5):
        print("Ön a Szénsavmentes Szentkirályi Ásványvizet választotta")
