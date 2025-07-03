class Solution:
    def getSum(self, a: int, b: int) -> int:
        while (b & 0xffffffff) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry 

        if b > 0:
            return a & 0xffffffff

        return a
