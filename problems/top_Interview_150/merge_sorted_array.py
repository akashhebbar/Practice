nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


def merge_sorted_array_brute_force(nums1, m, nums2, n):
    """
    Brute Force Approach:
    Time Complexity: O((m+n)log(m+n))
    Space Complexity: O(1)
    """
    # Copy nums2 elements to nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    # Sort the entire array
    nums1.sort()
    return nums1


def merge_sorted_array_better(nums1, m, nums2, n):
    """
    Better Approach:
    Time Complexity: O(m+n)
    Space Complexity: O(m)
    """
    # Create a copy of nums1
    nums1_copy = nums1[:m]
    p1 = 0  # pointer for nums1_copy
    p2 = 0  # pointer for nums2
    p = 0  # pointer for nums1

    # Compare and merge
    while p1 < m and p2 < n:
        if nums1_copy[p1] <= nums2[p2]:
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
        p += 1

    # Add remaining elements
    if p1 < m:
        nums1[p:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p:] = nums2[p2:]

    return nums1


def merge_sorted_array_optimal(nums1, m, nums2, n):
    """
    Optimal Approach:
    Time Complexity: O(m+n)
    Space Complexity: O(1)
    """
    p1 = m - 1  # pointer for nums1
    p2 = n - 1  # pointer for nums2
    p = m + n - 1  # pointer for merged array

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    return nums1


# Test all approaches
print(
    "Brute Force Approach:", merge_sorted_array_brute_force(nums1.copy(), m, nums2, n)
)
print("Better Approach:", merge_sorted_array_better(nums1.copy(), m, nums2, n))
print("Optimal Approach:", merge_sorted_array_optimal(nums1.copy(), m, nums2, n))
