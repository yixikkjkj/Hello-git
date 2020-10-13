class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        for c in s:
            if c in ('{', '[', '('):
                stack.append(c)
            elif c in ('}', ']', ')'):
                if not stack:
                    return False
                if pairs[c] != stack.pop(len(stack) - 1):
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True
