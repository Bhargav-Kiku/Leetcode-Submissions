class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord('a')] += 1
        for ch in target:
            f[ord(ch) - ord('a')] -= 1
        bad = sum(x < 0 for x in f)
        mx = -1
        for c in range(26):
            if f[c]:
                mx = c
        for i in range(len(target) - 1, -1, -1):
            cur = ord(target[i]) - ord('a')
            f[cur] += 1
            if f[cur] == 0:
                bad -= 1
            elif f[cur] == 1:
                mx = max(mx, cur)
            if bad or mx <= cur:
                continue
            nxt = cur + 1
            while nxt < 26 and not f[nxt]:
                nxt += 1
            if nxt == 26:
                continue
            f[nxt] -= 1
            res = list(target[:i])
            res.append(chr(nxt + ord('a')))
            for c in range(26):
                res.extend(chr(c + ord('a')) * f[c])
            return ''.join(res)
        return ""