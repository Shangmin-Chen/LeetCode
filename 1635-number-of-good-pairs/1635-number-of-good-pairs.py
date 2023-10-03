class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        from math import comb
        d = defaultdict(int)
        t = 0
        for i in nums:
            d[i] += 1
        for i in d:
            if d[i] > 2:
                t += comb(d[i],2)
            elif d[i] == 2:
                t += 1
        return t
        
        