from os import * 

bandName : str = None
favouriteSong : str = None
songLength : int = None

print("Kérem a kedvenc együttesének a nevét: ")
bandName = str(input())

print(f"Melyik a kedvenc dala a/az {bandName} együttestől?")
favouriteSong = str(input())

print(f"A {favouriteSong} című számnak mennyi a hossza? (percben)")
songLength = int(input())

system('cls')

print(f"Az ön kedvenc együttesének a neve {bandName}, a legjobb száma {favouriteSong}, aminek a hossza {songLength} perc!")