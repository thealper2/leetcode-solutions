from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        l = len(nums[0])

        for i in range(n):
            nums[i] = int(nums[i], 2)

        for i in range(0, max(nums) + 2):
            if i not in nums:
                result = []
                while i >= 1:
                    result.append(str(i % 2))
                    i //= 2

                s = ''.join(result[::-1])
                return (l - len(s)) * "0" + s

        return ''
