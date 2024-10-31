class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums.index(target)
