from colored import *

def readNameFromConsole()->str:
    name:str=None
    
    while(name==None or len(name)<2):
        print("Név: ", end="")
        name=input()
        if (len(name)<2):
            print("Nem nevet adott meg!")

    return name.capitalize().strip()


def welcomingMessage(name:str)->None:
    color=len(name)
    print(f"%s Üdvözlom {name}%s" % (fg(color), attr(0)))
