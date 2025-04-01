from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            
            if num + k in d:
                count += d[num + k]

            if num - k in d:
                count += d[num - k]

            d[num] += 1

        return count