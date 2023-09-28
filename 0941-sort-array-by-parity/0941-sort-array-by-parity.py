class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        i = 0
        while i < len(nums):
            if nums[i]%2 == 0:
                l.append(nums[i])
                nums.pop(i)
            else:
                i+=1
        for j in nums:
            l.append(j)
        return l