def convertCelsToOther(celTemp: int, tempChoice: str) -> int:
    convertedTemp: int = None

    if (tempChoice == "K"):
        convertedTemp = celTemp + 273.15
    elif (tempChoice == "F"):
        convertedTemp = 9 / 5 * celTemp + 32 

    return convertedTemp

    