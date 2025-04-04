from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1):
            result += self.nums[i]

        return result