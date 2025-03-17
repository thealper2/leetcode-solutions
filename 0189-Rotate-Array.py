from typing import List


def rotate(nums: List[int], k: int) -> None:
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop()
    return nums
