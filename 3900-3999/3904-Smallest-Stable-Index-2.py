class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_nums = [nums[0]]
        for i in range(1, n):
            max_nums.append(max(nums[i], max_nums[-1]))

        min_nums = [nums[-1]]
        for i in range(n - 2, -1, -1):
            min_nums.append(min(nums[i], min_nums[-1]))

        min_nums.reverse()
        for i in range(n):
            score = max_nums[i] - min_nums[i]
            if score <= k:
                return i

        return -1
