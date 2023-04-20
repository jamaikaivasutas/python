def getTempFromConsole() -> int:
    temperature: int = None
    temporary: str = None

    while (temperature == None):
        print("Kérem adjon meg egy hőmérsékletet Celsiusban! ", end="")
        temporary = input()
        if (temporary.isnumeric()):
            temperature = int(temporary)
    return temperature

def getTempTypeFromConsole() -> str:
    tempType: str = None

    while (tempType == None or (tempType != "F" and tempType != "K")):
        print("Kérem adja meg, mibe akarja átváltani!\n [K] Kelvin\n [F] Fahrenheit\n ", end="")
        tempType = input()

    return tempType