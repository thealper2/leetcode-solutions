from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        distance = float('inf')
        nums.sort()

        for i in range(n - 2):
            l, r = i + 1, n - 1
            new_target = target - nums[i]

            while l < r:
                current_sum = nums[l] + nums[r]

                if abs(distance) > abs(new_target - current_sum):
                    distance = new_target - current_sum

                if current_sum == new_target:
                    return target

                elif current_sum < new_target:
                    l += 1
                else:
                    r -= 1

        return target - distance

        