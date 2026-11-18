from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        count = 0
        for v, idxs in positions.items():
            if len(idxs) == 3 and idxs[1] - idxs[0] == idxs[2] - idxs[1]:
                count += 1
        return count
