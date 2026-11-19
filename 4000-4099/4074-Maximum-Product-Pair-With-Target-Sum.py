class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        best = None
        best_prod = None
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if nums[i] + nums[j] == target and nums[i] > nums[j]:
                    prod = nums[i] * nums[j]
                    if best_prod is None or prod > best_prod:
                        best_prod = prod
                        best = [i, j]
        return best if best is not None else [-1, -1]