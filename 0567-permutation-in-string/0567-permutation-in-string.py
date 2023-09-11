from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = Counter(s1)
        for i in range(len(s2)):
            dict2 = Counter(s2[i:i+len(s1)])
            if dict1 == dict2:
                return True
        return False