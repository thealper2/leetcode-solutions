from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = {}
        max_count = 0
        max_num = -1
        n = len(nums)
        
        for i in range(n):
            if nums[i] not in counts and nums[i] % 2 == 0:
                counts[nums[i]] = 1
            elif nums[i] % 2 == 0:
                counts[nums[i]] += 1

        for num, count in counts.items():
            if count > max_count:
                max_count = count
                max_num = num

            elif count == max_count:
                max_num = min(num, max_num)
        
        return max_num
