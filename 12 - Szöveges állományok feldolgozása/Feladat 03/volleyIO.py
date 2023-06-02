from volley import Volley
from typing import *
import os


def readBooksFromFile(fileName: str) -> List[Volley]:
    volleys: List[Volley] = []
    volley: Volley = None

    fileName: str ="data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t')
        
                volley = Volley()
                volley.playerName = data[0]
                volley.playerHeight = data[1]
                volley.playerPost = data[2]
                volley.playerNationality = data[3]
                volley.playerTeam = data[4]
                volley.playerCountry = data[5]
            
                volleys.append(volley)

        return volleys
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def writeBooksToFile(fileName: str, books: List[Volley]) -> None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="w") as file:
            for volley in books:
                file.write(f"{volley.playerName}\t{volley.playerHeight}\t{volley.playerPost}\t{volley.playerNationality}\t{volley.playerTeam}\t{volley.playerCountry}\n")

    except FileNotFoundError as ex:
        print(f"{ex.filename} itasakor hiba lepett fel!")