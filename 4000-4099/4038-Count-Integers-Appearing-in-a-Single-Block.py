class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        first = {}
        last = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            last[num] = i

        special_count = 0
        for num in first:
            start = first[num]
            end = last[num]
            is_contiguous = True
            for i in range(start, end + 1):
                if nums[i] != num:
                    is_contiguous = False
                    break

            if is_contiguous:
                special_count += 1

        return special_count