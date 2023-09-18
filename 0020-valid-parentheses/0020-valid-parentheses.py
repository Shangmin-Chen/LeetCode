class Solution:
    def isValid(self, s: str) -> bool:
        openclose = {'(':')', '[':']', '{':'}'}
        opens = ['(','[','{'] 
        closes = [')',']','}']
        stack = []
        i = 0
        length = len(s)
        while i < length:
            if s[i] in opens:
                stack.append(s[i])
            elif s[i] in closes:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if openclose[popped] != s[i]:
                    return False
            i += 1
        if len(stack) != 0:
            return False
        return True