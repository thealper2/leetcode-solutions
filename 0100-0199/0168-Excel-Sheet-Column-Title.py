class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            c = chr(remainder + 65)
            result = c + result
            columnNumber //= 26

        return result
