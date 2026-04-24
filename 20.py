class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        chMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c not in chMap: #左括号直接入栈
                stack.append(c)
            elif not stack:
                return False
            else:
                leftC = stack.pop()
                if chMap[c] != leftC:
                    return False
        return not stack
