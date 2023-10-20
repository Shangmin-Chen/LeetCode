class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                a =s.pop()
                b =s.pop()
                s.append(b - a)
            elif i == '*':
                s.append(s.pop() * s.pop())
            elif i == '/':
                a =s.pop()
                b =s.pop()
                s.append(int(b / a))
            else:
                s.append(int(i))
        return s[0]