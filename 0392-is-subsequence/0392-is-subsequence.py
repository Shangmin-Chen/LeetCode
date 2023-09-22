class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=""
        for i in s:
            while len(t) > 0:
                if i == t[0]:
                    x += i
                    t=t[1:]
                    break
                t=t[1:]
        if x == s:
            return True
        return False