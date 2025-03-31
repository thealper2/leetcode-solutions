from typing import List


def calPoints(operations: List[int]) -> int:
    res = []
    idx = -1
    for operation in operations:
        # print(idx, res)
        if operation == "C":
            res.pop()
            idx -= 1
        elif operation == "D":
            res.append(int(res[idx]) * 2)
            idx += 1
        elif operation == "+":
            res.append(int(res[idx]) + int(res[idx - 1]))
            idx += 1
        else:
            res.append(int(operation))
            idx += 1
    return sum(res)
