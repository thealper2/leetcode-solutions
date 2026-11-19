from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        result = []
        while counts:
            present = sorted(counts.keys())
            result.extend(present)
            for i in present:
                counts[i] -= 1
                if counts[i] == 0:
                    del counts[i]

        return result