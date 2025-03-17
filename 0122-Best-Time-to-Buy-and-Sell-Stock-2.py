from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if min_price < price:
            max_profit += price - min_price

        min_price = price

    return max_profit
