def searchCommonLetters(firstWord: str, secondWord: str) -> str:
    intersection: str = ""
    
    for x in firstWord:
        y: bool = secondWord.find(x) != -1
        z: bool = intersection.find(x) == 0 
        if (y and not z):
            intersection += x
            
    return intersection
