from collections import defaultdict


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        s = 0
        for k, v in counts.items():
            if v == 1:
                s += k

        return s
