class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        zeros = nums.count(0)
        start = n - zeros

        swaps = 0
        for i in range(start, n):
            if nums[i] != 0:
                swaps += 1

        return swaps