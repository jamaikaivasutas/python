from os import * 

bandName : str = None
favouriteSong : str = None
songLength : int = None

print("Kérem a kedvenc együttesének a nevét: ",end="")
bandName = str(input())

print(f"Melyik a kedvenc dala a/az {bandName} együttestől?",end="")
favouriteSong = str(input())

print(f"A {favouriteSong} című számnak mennyi a hossza? (percben)",end="")
songLength = int(input())

system('cls')

print(f"Az ön kedvenc együttesének a neve {bandName}, a legjobb száma {favouriteSong}, aminek a hossza {songLength} perc!")