from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum < min_sum:
                min_sum = current_sum

        start_value = 1 - min_sum
        return max(start_value, 1)