class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1

        m = set()
        for num in nums:
            if num > k:
                m.add(num)

        return len(m)
