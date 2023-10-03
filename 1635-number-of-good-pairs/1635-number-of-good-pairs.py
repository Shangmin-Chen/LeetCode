class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a,b,o=0,0,0
        while a<len(nums)-1:
            b+=1
            if nums[a] == nums[b]:
                o+=1
            if b == len(nums)-1:
                a+=1
                b=a
            
        return o
                
