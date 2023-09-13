class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = nums.count(0)
        w = nums.count(1)
        b = nums.count(2)
        for i in range(len(nums)):
            if i < r:
                nums[i] = 0
            elif i < r+w:
                nums[i] = 1
            elif i < r+w+b:
                nums[i] = 2

        