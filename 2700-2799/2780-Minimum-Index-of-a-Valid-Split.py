from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        dominant = None
        for num, count in freq.items():
            if count * 2 > n:
                dominant = num
                break

        if dominant is None:
            return -1

        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1

            right_count = freq[dominant] - left_count
            left_len = i + 1
            right_len = n - left_len
            if left_count * 2 > left_len and right_count * 2 > right_len:
                return i

        return -1
