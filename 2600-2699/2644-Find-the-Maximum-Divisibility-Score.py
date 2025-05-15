from collections import defaultdict
from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        max_count = -1
        result = -1

        for d in sorted(set(divisors)):
            count = 0
            for num in freq:
                if num % d == 0:
                    count += freq[num]

            if count > max_count or (count == max_count and d < result):
                max_count = count
                result = d

        return result