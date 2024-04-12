from typing import List

def removeDuplicates(nums: List[int]) -> int:
    uniq = []
    for i in nums:
        if i not in uniq:
            uniq.append(i)

    for i in uniq:
        c = nums.count(i)
        while c > 2:
            nums.remove(i)
            c = c - 1

    #print(nums)
    return len(nums)
