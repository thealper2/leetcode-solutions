class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices = sorted(prices, reverse=True)
        discounts = sorted(discounts, reverse=True)
        n = len(discounts)
        total = 0
        
        for i, price in enumerate(prices):
            if i < n:
                discount = discounts[i]
                total += price * (100 - discount) / 100
            else:
                total += price

        return total