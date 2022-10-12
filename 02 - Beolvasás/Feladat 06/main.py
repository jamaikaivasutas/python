from os import *

releaseDate : int = None
directorName : str = None
movieName : str = None
protagonistName : str = None

print("Kérem a film megjelenésének az évét!",end="")
releaseDate = int(input())

print("Kérem a film rendezőjének nevét!",end="")
directorName = str(input())

print("Kérem a film címét!",end="")
movieName = str(input())

print(f"Kérem a {movieName} című film főszereplőjét játszó színésznek a nevét",end="")
protagonistName = str(input())

system('cls')

print(f"{releaseDate}-ban {directorName} rendezésében megjelent a/az {movieName} című film {protagonistName} főszereplésével!")