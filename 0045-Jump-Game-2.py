from typing import List


def jump(nums: List[int]) -> bool:
    idx = 0
    last = 0
    res = 0
    for i in range(len(nums) - 1):
        idx = max(idx, i + nums[i])
        # print(i, idx, num)
        if i == last:
            last = idx
            res += 1

    return res
