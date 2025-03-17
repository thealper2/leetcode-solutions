from typing import List


def removeElement(nums: List[int], val: int) -> int:
    val_count = nums.count(val)
    while val_count != 0:
        nums.remove(val)
        val_count = val_count - 1
    print(nums)
    return len(nums)
