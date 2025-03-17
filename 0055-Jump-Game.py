from typing import List


def canJump(nums: List[int]) -> bool:
    idx = 0
    for i, num in enumerate(nums):
        if i <= idx:
            print(i, idx, num)
            idx = max(idx, i + num)

    if idx >= len(nums) - 1:
        return True
    else:
        return False
