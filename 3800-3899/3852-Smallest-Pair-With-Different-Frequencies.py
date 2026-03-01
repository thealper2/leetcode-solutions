from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return [-1, -1]

        freq = Counter(nums)
        unique_values = sorted(freq.keys())

        n = len(unique_values)
        if n < 2:
            return [-1, -1]

        for i in range(n - 1):
            x = unique_values[i]
            for j in range(i + 1, n):
                y = unique_values[j]
                if freq[x] != freq[y]:
                    return [x, y]

        return [-1, -1]
