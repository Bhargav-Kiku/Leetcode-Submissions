class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c = 0
        l = False
        m0 = False
        for i in s:
            if i == '1':
                if not l:
                    l = True
            else:
                if l:
                    l = False
                    m0 = True
            if m0 and l: return False
        return True