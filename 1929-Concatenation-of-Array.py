from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (len(nums) * 2)

        for i in range(len(result)):
            result[i] = nums[i % len(nums)]

        return result
