from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        match = True
        while match:
            for num in nums:
                if num == original:
                    original *= 2
                    match = True
                    break

                match = False

        return original