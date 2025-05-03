from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = nums[::2]
        odd = nums[1::2]

        even.sort()
        odd.sort(reverse=True)

        result = []
        for e_d, o_d in zip(even, odd):
            result.append(e_d)
            result.append(o_d)

        if len(even) > len(odd):
            result.append(even[-1])

        return result

