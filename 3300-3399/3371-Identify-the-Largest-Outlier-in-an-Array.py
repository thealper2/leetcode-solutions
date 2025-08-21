class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        num_count = {}
        for x in nums:
            num_count[x] = num_count.get(x, 0) + 1

        largest = float('-inf')
        for s in nums:
            o = total - 2 * s
            if o in num_count:
                if o == s and num_count[o] < 2:
                    continue

                largest = max(largest, o)

        return largest
