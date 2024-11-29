# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def helper(left, right):
            if left == right:
                return left
            
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                return helper(left, mid)
            else:
                return helper(mid + 1, right)

        return helper(1, n)