class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletions = 0
        prev = None
        for num in nums:
            if prev is not None and prev == num:
                deletions += 1
            else:
                prev = num

        return deletions