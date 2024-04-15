from typing import List

def largestPerimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)
    l = 0
    for i in range(len(nums) - 2):
        a = nums[i]
        b = nums[i + 1]
        c = nums[i + 2]
        if a < b + c:
            l = a + b + c
            break

    return l
