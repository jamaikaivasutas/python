from os import *

whichSoda: input("Melyik üdítőt választja? \n 1 - Coca Cola \n 2 - Pepsi \n 3 - Fanta \n 4 - Sprite \n ")

match whichSoda: 
    case "1":
        print("Ön a Coca Cola-t választotta!")
    case "2":
        print("Ön a Pepsit választotta")
    case "3":
        print("Ön a Fantát választotta")
    case "4":
        print("Ön a Spirte-ot válaszotta")
    case _: 
        print("Ilyen üdítő nincsen az automatában")