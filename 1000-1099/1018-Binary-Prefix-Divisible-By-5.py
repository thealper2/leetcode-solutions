from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        prev = 0
        for num in nums:
            prev = (prev * 2 + num) % 5
            result.append(prev == 0)

        return result
