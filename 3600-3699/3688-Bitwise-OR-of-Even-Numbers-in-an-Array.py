from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if not num % 2:
                result |= num

        return result
