from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd_max = max([v for v in count.values() if v % 2 == 1])
        even_min = min([v for v in count.values() if v % 2 == 0])
        return odd_max - even_min
