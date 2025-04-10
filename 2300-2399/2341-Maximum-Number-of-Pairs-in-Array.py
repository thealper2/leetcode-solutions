from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        c = 0

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                if d[num] >= 2:
                    d.pop(num)
                    c += 1

        return [c, len(d.keys())]