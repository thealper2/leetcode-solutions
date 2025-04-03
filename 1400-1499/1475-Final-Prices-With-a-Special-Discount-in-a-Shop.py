def finalPrices(prices):
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break

    return prices

print(finalPrices([8,4,6,2,3]))
print(finalPrices([1,2,3,4,5]))
print(finalPrices([10,1,1,6]))