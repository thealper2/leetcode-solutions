class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1