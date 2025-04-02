# def max_profit(prices):
#     if not prices or len(prices) < 2:
#         return 0

#     min_price = float("inf")
#     max_profit = 0

#     for price in prices:
#         # Update minimum price seen so far
#         min_price = min(min_price, price)
#         # Calculate potential profit if we sell at current price
#         current_profit = price - min_price
#         # Update maximum profit if current profit is higher
#         max_profit = max(max_profit, current_profit)

#     return max_profit


def max_profit(prices):
    """
    Most optimized solution for Best Time to Buy and Sell Stock
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(prices) < 2:
        return 0

    buy = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < buy:
            buy = price
        else:
            max_profit = max(max_profit, price - buy)

    return max_profit


# Test cases with different scenarios
test_cases = [
    [7, 1, 5, 3, 6, 4],  # Normal case with multiple opportunities
    [7, 6, 4, 3, 1],  # Decreasing prices
    [2, 4, 1],  # Minimum at the end
    [1, 2, 3, 4, 5],  # Increasing prices
    [5, 4, 3, 2, 1],  # Strictly decreasing
    [1, 1, 1, 1, 1],  # All same prices
    [2, 2, 5, 0, 0, 3, 1, 4],  # Complex case with multiple peaks
]

# Run test cases with detailed output
for i, prices in enumerate(test_cases, 1):
    result = max_profit(prices)
    print(f"\nTest Case {i}:")
    print(f"Input: {prices}")
    print(f"Maximum Profit: {result}")
    print("-" * 50)
