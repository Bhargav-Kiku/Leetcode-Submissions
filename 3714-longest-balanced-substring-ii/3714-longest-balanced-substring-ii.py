class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res, l = 1, 1
        for c0, c1 in pairwise(s):
            if c0 == c1: l += 1
            else:
                res = max(res, l)
                l = 1
        res = max(res, l)
        ab, bc, ca, abc = {}, {}, {}, {}
        abc[(0, 0)] = ab[(0, 0)] = bc[(0, 0)] = ca[(0, 0)] = -1
        x = [0, 0, 0]
        for i, c in enumerate(s):
            x[ord(c) - 97] += 1
            A, B, C = x
            key = (B - A, C - A)
            if key in abc: res = max(res, i - abc[key])
            else: abc[key] = i
            key = (A - B, C)
            if key in ab: res = max(res, i - ab[key])
            else: ab[key] = i
            key = (B - C, A)
            if key in bc: res = max(res, i - bc[key])
            else: bc[key] = i
            key = (C - A, B)
            if key in ca: res = max(res, i - ca[key])
            else: ca[key] = i
        return res