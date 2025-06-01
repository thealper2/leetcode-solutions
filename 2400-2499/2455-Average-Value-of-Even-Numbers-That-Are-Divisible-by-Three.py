from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = 0
        count_nums = 0

        for i in range(n):
            if nums[i] % 6 == 0:
                sum_nums += nums[i]
                count_nums += 1

        if count_nums == 0:
            return 0

        return sum_nums // count_nums