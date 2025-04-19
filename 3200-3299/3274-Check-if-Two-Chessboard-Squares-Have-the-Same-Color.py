def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:
    x1 = ord(coordinate1[0])
    y1 = int(coordinate1[1])
    
    x2 = ord(coordinate2[0])
    y2 = int(coordinate2[1])

    s1 = x1 + y1
    s2 = x2 + y2

    return s1 % 2 == s2 % 2


print(checkTwoChessboards(coordinate1 = "a1", coordinate2 = "c3"))
print(checkTwoChessboards(coordinate1 = "a1", coordinate2 = "h3"))