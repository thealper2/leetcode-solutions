from typing import List


def moveZeroes(nums: List[int]) -> None:
    zero_count = nums.count(0)
    while zero_count > 0:
        nums.remove(0)
        zero_count -= 1
        nums.append(0)

    # print(nums)
