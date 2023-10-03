class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        t = 0
        for i in nums:
            d[i] += 1
            t += d[i]-1
        return t
        
        