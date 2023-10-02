class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        c = 0
        l = len(colors) - 2
        while c < l:
            if c == l/2:
                if "AAA" not in colors:
                    return False
                elif "BBB" not in colors:
                    return True
            if colors[c:c+3] == "AAA":
                a += 1
            elif colors[c:c+3] == "BBB":
                b += 1
            c += 1
        if a <= b:
            return False
        else:
            return True
