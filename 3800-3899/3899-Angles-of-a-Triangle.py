import math

class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sorted(sides)

        if a + b <= c or a + c <= b or b + c <= a:
            return []

        angleA = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angleB = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angleC = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        return [math.degrees(angleA), math.degrees(angleB), math.degrees(angleC)]
