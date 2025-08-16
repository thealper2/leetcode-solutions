from itertools import permutations
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max_num = 0
        binaries = [bin(num)[2:] for num in nums]
        for perm in permutations(binaries):
            concatenated = ''.join(perm)
            if concatenated[0] == '0':
                continue

            max_num = max(max_num, int(concatenated, 2))

        return max_num
