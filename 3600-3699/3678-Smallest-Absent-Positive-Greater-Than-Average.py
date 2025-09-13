from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        if not nums:
            return 1

        n = len(nums)
        total = sum(nums)
        avg = total / n

        positive_nums = sorted(set(x for x in nums if x > 0))
        if not positive_nums:
            return 1

        candidate = int(avg) + 1
        if candidate <= 0:
            candidate = 1

        seen = set(nums)
        while candidate in seen:
            candidate += 1

        return candidate
