class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur = -math.inf
        ans = 0
        for i in sorted(pairs, key=lambda x: x[1]):
            if i[0] > cur:
                ans += 1
                cur = i[1]
        return ans

        