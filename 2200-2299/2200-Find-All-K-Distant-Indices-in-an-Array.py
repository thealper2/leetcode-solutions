from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        k_distant = []
        indexes = []

        for i in range(n):
            if nums[i] == key:
                indexes.append(i)

        for i in range(n):
            for idx in indexes:
                if abs(idx - i) <= k:
                    k_distant.append(i)
                    break

        return k_distant