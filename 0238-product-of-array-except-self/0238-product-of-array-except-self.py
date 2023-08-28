class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution uses dp, time comp :O(n)
        sol=[1]*len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            sol[i] *= prefix
            prefix = prefix*nums[i]
            sol[len(nums)-i-1] *= postfix
            postfix = postfix*nums[len(nums)-i-1]
        return(sol)