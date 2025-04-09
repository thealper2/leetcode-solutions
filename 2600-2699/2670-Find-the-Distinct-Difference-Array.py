from typing import List


def distinctDifferenceArray(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [0] * n
    suffix = [0] * n
    
    seen = set()
    for i in range(n):
        seen.add(nums[i])
        prefix[i] = len(seen)
    
    seen = set()
    for i in range(n - 1, -1, -1):
        suffix[i] = len(seen)
        seen.add(nums[i])
    
    diff = []
    for i in range(n):
        diff.append(prefix[i] - suffix[i])
    
    return diff