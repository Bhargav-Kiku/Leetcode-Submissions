class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        e1 = []
        o1 = []
        e2 = []
        o2 = []
        n = len(s1)
        for i in range(n):
            if i & 1:
                o1.append(s1[i])
            else:
                e1.append(s1[i])
        for i in range(n):
            if i & 1:
                o2.append(s2[i])
            else:
                e2.append(s2[i])
        o1.sort()
        o2.sort()
        if o1 != o2: return False
        e1.sort()
        e2.sort()
        return e1 == e2