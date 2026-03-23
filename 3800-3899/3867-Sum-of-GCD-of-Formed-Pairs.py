import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mxi = 0
        prefix_gcd = []
        for i in range(n):
            num = nums[i]
            mxi = max(mxi, num)
            prefix_gcd.append(math.gcd(num, mxi))

        prefix_gcd.sort()
        total = 0
        l, r = 0, len(prefix_gcd) - 1
        while l < r:
            total += math.gcd(prefix_gcd[l], prefix_gcd[r])
            l += 1
            r -= 1

        return total
