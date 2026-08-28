class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord('a')] += 1
        mid = ""
        for i in range(26):
            if f[i] % 2 == 1:
                if mid:
                    return ""
                mid = chr(ord('a') + i)
            f[i] //= 2
        hl = n // 2
        half = []
        found = 0
        while found < hl:
            c = ord(target[found]) - ord('a')
            if f[c] == 0:
                break
            f[c] -= 1
            half.append(chr(ord('a') + c))
            found += 1
        i = found
        while i >= 0:
            if i < hl:
                start = ord(target[i]) - ord('a') + 1
                for c in range(start, 26):
                    if f[c] == 0:
                        continue
                    f[c] -= 1
                    suf = []
                    for j in range(26):
                        suf.append(
                            chr(ord('a') + j) * f[j]
                        )
                    left = "".join(half[:i]) + chr(ord('a') + c) + "".join(suf)
                    cd = left + mid + left[::-1]
                    if cd > target:
                        return cd
                    f[c] += 1
            if i == hl:
                left = "".join(half)
                cd = left + mid + left[::-1]
                if cd > target:
                    return cd
            i -= 1
            if i >= 0:
                c = ord(half[i]) - ord('a')
                f[c] += 1
                half.pop()
        return ""