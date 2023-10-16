class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from math import comb
        l = []
        for i in range(rowIndex+1):
            l.append(comb(rowIndex,i))
        return l
