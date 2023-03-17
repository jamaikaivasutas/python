def readNameFromConsole()->str:
    name:str=""
    
    while(len(name)<2):
        print("Név: ", end="")
        name=input()
        if (len(name)<2):
            print("Nem nevet adott meg!")

    return name.capitalize().strip()

def readAgeFromConsole()->int:
    birthDate:int=None
    temp:str=None

    while(birthDate==None):
        print("Kérem adja meg a születési évé!")
        temp=input()
        if temp.isnumeric():
            birthDate=int(temp)
        else:
            print("Nem jo")

    return birthDate

def readDateFromConsole()->int:
    date:int=None
    temp:str=None

    while(date==None):
        print("Kérem adja meg az idei évet!")
        temp=input()
        if temp.isnumeric():
            date=int(temp)
        else:
            print("Nem jo")

    return date

def printWelcomingMessage(name:str, age:int)->None:
    print(f"{name} ön az idén {age} éves.")