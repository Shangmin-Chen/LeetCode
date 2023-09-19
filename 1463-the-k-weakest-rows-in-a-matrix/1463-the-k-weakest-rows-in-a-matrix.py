import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        x = []
        y = []
        for i in range(len(mat)):
            mat[i] = sum(mat[i])
        for i, j in enumerate(mat):
            x.append((j,i))
        x = sorted(x)
        for i in range(len(x)):
            y.append(x[i][1])
            k -= 1
            if k == 0:
                return y
