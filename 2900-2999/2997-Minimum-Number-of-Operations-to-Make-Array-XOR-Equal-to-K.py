from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_total = 0
        for num in nums:
            xor_total ^= num

        diff = xor_total ^ k
        return diff.bit_count()
