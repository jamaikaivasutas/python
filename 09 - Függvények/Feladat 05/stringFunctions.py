def searchCommonLetters(firstWord: str, secondWord: str) -> str:
    intersection: str = ""
    
    for x in firstWord:
        y: bool = secondWord.find(x) > 0
        z: bool = intersection.find(x) == 0 
        if (x and y):
            intersection += x
            
    return intersection
