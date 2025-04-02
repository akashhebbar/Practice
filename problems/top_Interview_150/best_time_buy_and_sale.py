prices = [7, 6, 4, 3, 1]


def max_profit(prices):
    max_profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        profit = prices[i] - buy
        if profit < 0:
            buy = prices[i]
        else:
            max_profit = max(max_profit, profit)
    return max_profit


print(max_profit(prices))
