from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        result = 0
        for key, value in freq.items():
            if value % k == 0:
                result += key * value

        return result
