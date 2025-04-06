from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        result = 0
        for num in nums:
            if num < 10:
                result += num
            else:
                result -= num

        return result != 0