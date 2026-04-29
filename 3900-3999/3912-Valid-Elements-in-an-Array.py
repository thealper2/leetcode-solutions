class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 0:
            return []

        left_valid = [False] * n
        left_max = float('-inf')
        for i in range(n):
            if nums[i] > left_max:
                left_valid[i] = True
                left_max = nums[i]

        right_valid = [False] * n
        right_max = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > right_max:
                right_valid[i] = True
                right_max = nums[i]

        result = []
        for i in range(n):
            if left_valid[i] or right_valid[i]:
                result.append(nums[i])

        return result