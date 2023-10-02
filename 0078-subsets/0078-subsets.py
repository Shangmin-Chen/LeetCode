class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        e = [[]]
        c =[list(combinations(nums,i)) for i in range(1, len(nums)+1)]
        for i in c:
            for j in i:
                e.append(list(j))
        return e
            