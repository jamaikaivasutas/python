def getTempFromConsole() -> int:
    temperature: int = None

    while (temperature == None):
        print("Kérem adjon meg egy hőmérsékletet Celsiusban!", end="")
        temperature = input()

    return temperature

