nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


# Brute Force Approach - Time: O(n*k), Space: O(1)
def brute_force_rotate(nums, k):
    n = len(nums)
    k = k % n
    for _ in range(k):
        last = nums[-1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last
    return nums


# Better Approach - Time: O(n), Space: O(n)
def better_rotate(nums, k):
    n = len(nums)
    k = k % n
    temp = nums.copy()
    for i in range(n):
        nums[(i + k) % n] = temp[i]
    return nums


# Optimal Approach - Time: O(n), Space: O(1)
def optimal_rotate(nums, k):
    n = len(nums)
    k = k % n

    # Reverse entire array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse first n-k elements

    reverse(0, n - k - 1)
    # Reverse last k elements
    reverse(n - k, n - 1)
    # Reverse entire array
    reverse(0, n - 1)
    return nums


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def right_rotate(nums, k):
    n = len(nums)
    k = k % n

    # For right rotation:
    # 1. Reverse first n-k elements
    reverse(nums, 0, n - k - 1)
    # 2. Reverse last k elements
    reverse(nums, n - k, n - 1)
    # 3. Reverse entire array
    reverse(nums, 0, n - 1)
    return nums


def left_rotate(nums, k):
    n = len(nums)
    k = k % n

    # For left rotation:
    # 1. Reverse first k elements
    reverse(nums, 0, k - 1)
    # 2. Reverse remaining n-k elements
    reverse(nums, k, n - 1)
    # 3. Reverse entire array
    reverse(nums, 0, n - 1)
    return nums


# Test all approaches
print("Original array:", nums)
print("\nTesting different rotation approaches:")
print("1. Brute Force:", brute_force_rotate(nums.copy(), k))
print("2. Better Approach:", better_rotate(nums.copy(), k))
print("3. Optimal Approach:", optimal_rotate(nums.copy(), k))

# Test both rotations
print("\nRight rotation by", k, "positions:", right_rotate(nums.copy(), k))
print("Left rotation by", k, "positions:", left_rotate(nums.copy(), k))
