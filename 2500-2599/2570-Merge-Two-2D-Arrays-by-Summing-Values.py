from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        sum_dict = {}

        for num in nums1:
            sum_dict[num[0]] = num[1]

        for num in nums2:
            sum_dict[num[0]] = sum_dict.get(num[0], 0) + num[1]

        result = []
        for k in sorted(sum_dict.items()):
            result.append(list(k))

        return result