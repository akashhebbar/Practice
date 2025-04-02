numbers = [2, 7, 11, 15]
target = 9


def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Find two numbers in a sorted array that add up to target.

    Args:
        numbers (List[int]): Sorted array of integers
        target (int): Target sum to find

    Returns:
        List[int]: 1-based indices of the two numbers that add up to target,
                  [-1, -1] if no solution exists
    """
    if len(numbers) < 2:
        return [-1, -1]

    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


print(two_sum(numbers, target))

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([], 5, [-1, -1]),
    ([1], 1, [-1, -1]),
    ([1, 2, 3, 4], 8, [-1, -1]),
]

for numbers, target, expected in test_cases:
    result = two_sum(numbers, target)
    print(f"Input: {numbers}, Target: {target}")
    print(f"Expected: {expected}, Got: {result}")
    print("Pass" if result == expected else "Fail")
    print("---")
