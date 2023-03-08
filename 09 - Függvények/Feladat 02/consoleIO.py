def readNameFromConsole() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem adja meg a nevét ", end="")
        name = input()
        
        if (len(name) < 2):
            print("Nem megfelelő a név.")

    return name.capitalize()
    
def printWelcomeMessage(name: str) -> None:
    print(f"Üdvözlöm {name}")
