# def max_profit(prices):
#     max_profit = 0
#     buy = prices[0]
#     for i in range(1, len(prices)):
#         profit = prices[i] - buy
#         if profit < 0:
#             buy = prices[i]
#         else:
#             max_profit = max(max_profit, profit)
#     return max_profit


# print(max_profit(prices))


def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = float("inf")
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# Test cases
test_cases = [
    [7, 1, 5, 3, 6, 4],  # Expected: 5
    [7, 6, 4, 3, 1],  # Expected: 0
    [2, 4, 1],  # Expected: 2
    [1, 2, 3, 4, 5],  # Expected: 4
    [5, 4, 3, 2, 1],  # Expected: 0
]

# Run test cases
for prices in test_cases:
    print(f"Prices: {prices}")
    print(f"Maximum Profit: {max_profit(prices)}\n")
