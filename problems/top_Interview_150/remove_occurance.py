nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


def remove_occurance_optimal(nums, val):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], "-"
            j -= 1
        else:
            i += 1
    return nums


print(remove_occurance_optimal(nums, val))
