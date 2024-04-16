def climbingStairs(n: int) -> int:
    # 0 -> 1
    # 1 -> 1 = 1 + 0
    # 2 -> 2 = 1 + 1
    # 3 -> 3 = 2 + 1
    # 4 -> 5 = 3 + 2
    # 5 -> 8 = 5 + 3
    # 6 -> 13 = 8 + 5
    f0 = 0
    f1 = 1
    for i in range(n):
        res = f0 + f1
        f0 = f1
        f1 = res

    return res
