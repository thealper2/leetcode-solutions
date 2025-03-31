def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        n = -n
        x = 1 / x

    res = 1

    while n > 0:
        if n % 2:
            res = res * x
        x = x * x
        n = n // 2

    return res
