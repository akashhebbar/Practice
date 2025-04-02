def majority_element(nums):
    """
    Find the majority element that appears more than n/2 times.
    Returns None if no majority element exists.
    """
    if not nums:
        return None

    majority = nums[0]
    count = 1

    # First pass: find potential majority element
    for i in range(1, len(nums)):
        if nums[i] == majority:
            count += 1
        else:
            count -= 1
            if count == 0:
                majority = nums[i]
                count = 1

    # Second pass: verify if it's actually a majority element
    count = 0
    for num in nums:
        if num == majority:
            count += 1

    # Check if it's actually a majority element
    if count > len(nums) // 2:
        return majority
    return None


# Test cases
test_cases = [
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],  # No majority element
    [2, 2, 1, 1, 1, 2, 2],  # Majority element is 2
    [3, 2, 3],  # Majority element is 3
    [1],  # Majority element is 1
]

for nums in test_cases:
    result = majority_element(nums)
    print(f"Array: {nums}")
    print(f"Majority element: {result}")
    print("-" * 30)
