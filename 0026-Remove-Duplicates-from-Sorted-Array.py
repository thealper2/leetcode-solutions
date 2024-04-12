def removeDuplicates(nums: List[int]) -> int:
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] = '_'
        elif nums[i] == nums[i-1]:
            nums[i] = '_'

    c = nums.count('_')
    while c != 0:
        nums.remove('_')
        c = c - 1
    print(nums)
    return len(nums)
