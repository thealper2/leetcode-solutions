class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        mid = nums[n // 2]
        return nums.count(mid) == 1
