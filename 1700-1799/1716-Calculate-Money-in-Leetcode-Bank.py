class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        day = 1
        
        for _ in range(n):
            total += week + day
            day += 1
            if day > 7:
                day = 1
                week += 1
        
        return total