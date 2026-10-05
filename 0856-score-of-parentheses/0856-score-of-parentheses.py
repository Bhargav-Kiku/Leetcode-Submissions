class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        dep = 0
        for i, ch in enumerate(s):
            if ch == '(':
                dep += 1
            else:
                dep -= 1
                if s[i - 1] == '(':
                    res += 1 << dep
        return res