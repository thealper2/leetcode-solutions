from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        result += 1

        return result