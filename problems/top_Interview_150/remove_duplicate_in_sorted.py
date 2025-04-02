# Test cases
nums1 = [1, 1, 2]  # Normal case
nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 4]  # Multiple duplicates


def remove_duplicate_in_sorted(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1
    return i + 1


print(remove_duplicate_in_sorted(nums))
