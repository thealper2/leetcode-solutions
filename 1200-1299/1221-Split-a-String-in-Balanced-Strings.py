class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = cL = cR = 0
        for c in s:
            if c == "L":
                cL += 1
            else:
                cR += 1

            if cL == cR:
                result += 1
                cL = 0
                cR = 0

        return result