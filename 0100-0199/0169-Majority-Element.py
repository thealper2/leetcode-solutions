from typing import List


def majorityElement(nums: List[int]) -> int:
    uniq = []
    for i in nums:
        if i not in uniq:
            uniq.append(i)

    major = 0
    for i in uniq:
        # print(i, nums.count(i))
        if nums.count(i) > nums.count(major):
            major = i

    return major
