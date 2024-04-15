def countOdds(low: int, high: int) -> int:
    if (low % 2 == 0 and high % 2 == 0):
        return int((high-low)/2)
    elif (low % 2 == 1 and high % 2 == 1):
        return int(1+(high-low)/2)
    else:
        return int(0.5+(high-low)/2)
