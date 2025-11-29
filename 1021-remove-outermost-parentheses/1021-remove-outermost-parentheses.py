class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        tr = []
        t = ""
        on = 0
        for i in s:
            if i == '(':
                on += 1
                t += '('
            else:
                on -= 1
                t += ')'
            if on == 0:
                tr.append(t)
                t = ""
        return ''.join(x[1:-1] for x in tr)