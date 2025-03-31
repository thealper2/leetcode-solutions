from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        for i in s:
            nums.remove(i)

        return nums