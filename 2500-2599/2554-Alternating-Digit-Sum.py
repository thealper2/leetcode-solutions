class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        r = 0
        c = 1

        for d in n:
            r += c * int(d)
            c = c * -1

        return r