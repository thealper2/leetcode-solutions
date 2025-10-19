from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = k
        while True:
            if num not in nums:
                return num

            num += k
