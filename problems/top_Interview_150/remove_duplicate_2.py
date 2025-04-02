nums = [1, 1, 1, 2, 2, 3]


def remove_duplicates(nums):
    if len(nums) <= 2:
        return nums
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return nums


print(remove_duplicates(nums))
