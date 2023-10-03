
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        diktator = {}
        ans = 0

        for i, num in enumerate(nums):
            if num not in diktator:
                diktator[num] = 0
            else:
                diktator[num] += 1
                ans += diktator[num]

        return ans