from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}

        for i in arr1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        result = []
        for i in arr2:
            result += [i] * d[i]
            d.pop(i)

        remaining = []
        for i in sorted(d.keys()):
            remaining += [i] * d[i]

        result += remaining
        return result