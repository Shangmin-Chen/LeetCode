class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0 or length == 1:
            return length
        pointerA = 0
        pointerB = 0
        chars = []
        counts = []
        count = 0
        
        while pointerA < length:
            curChar = s[pointerB]
            if curChar not in chars:
                chars.append(curChar)
                if pointerB == length - 1:
                    count += 1
                    counts.append(count)
                    count = 0
                    chars = []
                    pointerA += 1
                    pointerB = pointerA
                else:
                    count += 1
                    pointerB += 1
            else:
                counts.append(count)
                count = 0
                chars = []
                pointerA += 1
                pointerB = pointerA
            
                
        return max(counts)
            
            