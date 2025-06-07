class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for a in range(max(0, n - 2 * limit), min(limit, n) + 1):
            min_b = max(0, n - a - limit)
            max_b = min(limit, n - a)
            count += max(0, max_b - min_b + 1)
            
        return count