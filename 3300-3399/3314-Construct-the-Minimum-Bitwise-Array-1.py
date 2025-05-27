from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 0:
                result.append(-1)
                break

            found = -1
            for i in range(num):
                if (i | (i + 1)) == num:
                    found = i
                    break

            result.append(found)

        return result