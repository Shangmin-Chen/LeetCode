class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns = []
        nt = []
        for i in s:
            if i == "#":
                if len(ns) != 0:
                    ns.pop()
            else:
                ns.append(i)
        for i in t:
            if i == "#":
                if len(nt) != 0:
                    nt.pop()
            else:
                nt.append(i)
        return ns==nt
                
