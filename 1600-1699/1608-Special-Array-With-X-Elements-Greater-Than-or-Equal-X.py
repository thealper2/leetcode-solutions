from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        for x in range(n + 1):
            if x <= n and (x == n or nums[x] < x):
                if x == 0 or nums[x - 1] >= x:
                    return x
                else:
                    return -1

        return -1
