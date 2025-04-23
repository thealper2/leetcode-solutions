from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        p = int(n * 0.05)
        result = sum(arr[p:n-p])
        result /= n - (2 * p)
        return round(result, 5)
