class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peaks = 0
        valleys = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peaks += nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                valleys += nums[i]
        return peaks - valleys