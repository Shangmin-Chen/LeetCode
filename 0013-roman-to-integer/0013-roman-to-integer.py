class Solution:
    def romanToInt(self, s: str) -> int:
        x = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500,"M":1000, "IV":4, "IX":9, "XL":40,"XC":90, "CD":400, "CM":900}
        n = 0
        i = 0
        j = 1
        length = len(s)
        while i<length:
            if  j <length and s[i] + s[j] in x:
                n += x[s[i]+s[j]]
                i = j+1
                j += 1
            else:
                n += x[s[i]]
                i = j
            j += 1
        return n