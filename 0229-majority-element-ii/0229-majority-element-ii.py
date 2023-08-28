class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums)/3 and nums[i] not in newList:
                newList.append(nums[i])
        return newList