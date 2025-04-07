from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                if d[num] == 2:
                    result ^= num

        return result