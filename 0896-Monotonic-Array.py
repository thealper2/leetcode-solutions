from typing import List


def isMonotonic(nums: List[int]) -> bool:
    if len(nums) <= 1:
        return True

    increasing, decreasing = True, True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False

        if nums[i] > nums[i - 1]:
            decreasing = False

        if not increasing and not decreasing:
            return False

    return True
