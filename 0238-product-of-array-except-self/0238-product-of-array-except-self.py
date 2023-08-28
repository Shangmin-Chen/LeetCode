class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution uses dp, time comp :O(n)
        length=len(nums)
        sol=[1]*length
        prefix = 1
        postfix = 1
        for i in range(length):
            sol[i] *= prefix
            prefix = prefix*nums[i]
            sol[length-i-1] *= postfix
            postfix = postfix*nums[length-i-1]
        return(sol)