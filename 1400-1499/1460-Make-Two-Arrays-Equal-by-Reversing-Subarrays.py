from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for num in target:
            if num not in d:
                return False
            else:
                d[num] -= 1
                if d[num] < 0:
                    return False

        return True