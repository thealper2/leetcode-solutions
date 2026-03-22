class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even_count = sum(1 for x in nums1 if x % 2 == 0)
        odd_count = len(nums1) - even_count
        can_all_even = (odd_count == 0) or (odd_count >= 2)
        can_all_odd = (even_count == 0) or (even_count >= 1)
        return can_all_even or can_all_odd
