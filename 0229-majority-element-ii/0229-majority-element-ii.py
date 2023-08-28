class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        newList = []
        if len(nums)/3 < 1:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] in nums and nums.count(nums[i]) > 1:
                    nums.remove(nums[i])
            return nums
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums)/3 and nums[i] not in newList:
                newList.append(nums[i])
        return newList