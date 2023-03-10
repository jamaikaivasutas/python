def readFirstWordFromConsole() -> str:
    firstWord: str = None
    
    while firstWord == None:
        print("Kérek egy szót! " , end="")
        firstWord = input()
    
    return firstWord

def readSecondWordFromConsole() -> str:
    secondWord: str = None

    while secondWord == None:    
        print("Kérek egy másik szót! ", end="")
        secondWord = input()

    return secondWord

def printWordsToConsole(firstWord: str, secondWord: str) -> None:
    print()
