class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        o = 0
        for i in range(len(nums)):
            o += nums[i+1:].count(nums[i])
        return o
                