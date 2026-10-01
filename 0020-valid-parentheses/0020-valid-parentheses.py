class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in {'(','{','['}:
                stk.append(i)
            else:
                if stk:
                    ele = stk.pop()
                    if (ele=='(' and i!=')') or (ele=='{' and i!='}') or (ele=='[' and i!=']'):
                        return False
                else:
                    return False
        if stk:
            return False
        return True