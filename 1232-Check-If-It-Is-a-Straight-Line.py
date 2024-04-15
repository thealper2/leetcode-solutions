def checkStraightLine(coordinates: List[List[int]]) -> bool:
    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]
        if ((xi - coordinates[0][0]) * (coordinates[1][1] - coordinates[0][1])) != ((yi - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0])):
            return False

    return True
