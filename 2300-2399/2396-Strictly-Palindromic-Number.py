class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for num in range(2, n - 1):
            temp = ""
            while num >= 1:
                temp += str(num % 2)
                num //= 2
            
            if temp != temp[::-1]:
                return False
            
        return True