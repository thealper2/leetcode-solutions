class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = ord(coordinates[0])
        b = int(coordinates[1])

        if b % 2 == 0:
            if a % 2 == 0:
                return False
            else:
                return True
        else:
            if a % 2 == 0:
                return True
            else:
                return False