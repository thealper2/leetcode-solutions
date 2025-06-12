from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for num in nums:
            colors[num] += 1

        idx = 0
        for color in range(3):
            for _ in range(colors[color]):
                nums[idx] = color
                idx += 1
