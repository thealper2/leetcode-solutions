class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        for c in range(n):
            if num.count(str(c)) != int(num[c]):
                return False
            
        return True