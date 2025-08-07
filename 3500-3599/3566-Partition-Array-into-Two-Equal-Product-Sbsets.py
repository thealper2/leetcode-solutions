import math
from itertools import combinations
from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total_product = 1
        for num in nums:
            total_product *= num

        if total_product != target ** 2:
            return False

        n = len(nums)
        for r in range(1, n):
            for indices in combinations(range(n), r):
                subset1 = [nums[i] for i in indices]
                subset2 = [nums[i] for i in range(n) if i not in indices]

                prod1 = math.prod(subset1)
                prod2 = math.prod(subset2)

                if prod1 == target and prod2 == target:
                    return True

        return False
