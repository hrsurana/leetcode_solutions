class Solution:
    def isValid(self, s: str) -> bool:
        if not(s):
            return True
        if len(s)%2 != 0:
            return False
        
        open_close_map = {'}':'{', ']':'[', ')':'('}

        if s[0] in open_close_map.keys():
            return False

        stack = []
        for brackets in s:
            if brackets in ['{', '(', '[']:
                stack.append(brackets)
            else:
                if (not(stack) or stack[-1]!=open_close_map[brackets]):
                    return False
                stack.pop(-1)
        if not(stack):
            return True
        return False

