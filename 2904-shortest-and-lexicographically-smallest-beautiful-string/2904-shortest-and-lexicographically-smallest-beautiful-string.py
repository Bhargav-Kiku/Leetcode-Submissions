class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        ml = n
        i = 0
        c = 0
        for j in range(n):
            if s[j] == '1':
                c += 1
            while c > k or (c == k and s[i] == '0'):
                if s[i] == '1':
                    c -= 1
                i += 1
            if c == k:
                print("Pass")
                if j - i + 1 < ml:
                    res = s[i:j+1]
                    ml = j - i + 1
                elif j - i + 1 == ml:
                    if res == "":
                        res = s[i:j+1]
                        continue
                    res = min(res, s[i:j+1])
        return res