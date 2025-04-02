class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def brute_force(self):
        for i in range(0, len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
        return [-1, -1]

    def better_solution(self):
        self.nums.sort()
        right = len(self.nums) - 1
        left = 0
        while left < right:
            if self.nums[left] + self.nums[right] == self.target:
                return [left, right]
            elif self.nums[left] + self.nums[right] < self.target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

    def optimal_solution(self):
        hmap = {}
        for i, j in enumerate(self.nums):
            comp = self.target - j
            if comp in hmap:
                return [hmap[comp], i]
            hmap[j] = i
        return [-1, -1]


nums = [2, 11, 7, 15]
target = 9
obj = Solution(nums, target)
print(obj.brute_force())
print(obj.better_solution())
print(obj.optimal_solution())
