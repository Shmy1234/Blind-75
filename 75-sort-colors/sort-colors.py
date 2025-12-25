class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = nums.count(0)
        w = nums.count(1)
        b = nums.count(2)
        for i in range(r):
            nums[i] = 0
        for i in range(w):
            nums[r + i] = 1
        for i in range(b):
            nums[r + w + i] = 2