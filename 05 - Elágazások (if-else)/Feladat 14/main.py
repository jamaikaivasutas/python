from os import *

numberX: int = None
numberY: int = None
numberZ: int = None

system('cls')

print("Kérem az X számot!")
numberX = int(input())

print("Kérem az Y számot!")
numberY = int(input())

print("Kérem a Z számot!")
numberZ = int(input())

system('cls')

if numberX % numberY == 0 and numberX % numberZ != 0:
    print("Az X osztható Y-al!")
elif numberX % numberY != 0 and numberX % numberZ == 0: 
    print("Az X osztható Z-vel")
elif numberX % numberY == 0 and numberX % numberZ == 0:
    print("Az X az Y-al és a Z-vel is osztható!")