class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            cur_and = nums[i]
            cur_min = nums[i]
            for j in range(i, n):
                if j > i:
                    cur_and &= nums[j]
                    cur_min = min(cur_min, nums[j])
                if cur_and == cur_min:
                    total += 1
        return total