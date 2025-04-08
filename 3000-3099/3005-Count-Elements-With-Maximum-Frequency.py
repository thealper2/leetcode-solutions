from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        max_freq = max(d.values()) if d else 0
        return sum(freq for freq in d.values() if freq == max_freq)