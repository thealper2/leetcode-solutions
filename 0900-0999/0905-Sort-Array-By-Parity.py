from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            else:
                if nums[l] % 2 == 0:
                    l += 1
                
                if nums[r] % 2 == 1:
                    r -= 1

        return nums