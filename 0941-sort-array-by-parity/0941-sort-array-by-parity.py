class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        
        for i in nums:
            if i%2==0:
                l.append(i)
        for i in nums:
            if i%2==1:
                l.append(i)
        return l