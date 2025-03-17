from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    max = 0
    for account in accounts:
        if max < sum(account):
            max = sum(account)
    return max
