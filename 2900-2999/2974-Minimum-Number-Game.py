from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        while nums:
            alice = nums.pop(0)
            if nums:
                bob = nums.pop(0)
                result.append(bob)

            result.append(alice)

        return result