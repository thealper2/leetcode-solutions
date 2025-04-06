from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = float('-inf')
        for num in nums:
            if num > m:
                m = num

        r = (m + (k - 1)) * ((m + k) / 2) - ((m - 1) * ((m / 2)))
        return int(r)