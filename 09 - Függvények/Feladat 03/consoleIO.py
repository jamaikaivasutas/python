def age(datestr: str) -> int:
    size = len(datestr)
    yearLenght = len(datestr) - 4
    year = datestr[:size - yearLenght]
    yearInt = int(''.join(filter(str.isdigit, year)))
    age = 2023 - yearInt
    return age