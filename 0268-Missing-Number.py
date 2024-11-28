class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = (n * (n + 1)) / 2
        for num in nums:
            result -= num

        return int(result)