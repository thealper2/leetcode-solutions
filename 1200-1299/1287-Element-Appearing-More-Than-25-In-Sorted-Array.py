from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        p = n / 4
        counts = {}
        result = None

        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            
            if counts[num] >= p:
                result = num

        return result