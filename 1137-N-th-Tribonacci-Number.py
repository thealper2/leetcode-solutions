def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    nums = [0, 1, 1]

    for i in range(3, n + 1):
        next_num = nums[i - 1] + nums[i - 2] + nums[i - 3]
        nums.append(next_num)

    return nums[n]
