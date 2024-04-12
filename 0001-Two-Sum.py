from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    l = len(nums)
    for i in range(l):
        for j in range(l):
            tot = nums[i] + nums[j]
            if tot == target and i != j:
                return [i, j]
    return nums
