class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        f = Counter(s)
        hf = {}
        mid = ""
        m = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            if f[char] > 0:
                if f[char] % 2 != 0:
                    mid += char
                hf[char] = f[char] // 2
                m += hf[char]
        def getWays(f, target_k):
            ws = 1
            cl = 0
            for char in "abcdefghijklmnopqrstuvwxyz":
                count = f.get(char, 0)
                if count > 0:
                    cl += count
                    ws *= math.comb(cl, count)
                    if ws > target_k:
                        return target_k + 1
            return ws
        if getWays(hf, k) < k:
            return ""
        temp = []
        for _ in range(m):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if hf.get(char, 0) > 0:
                    hf[char] -= 1
                    ws = getWays(hf, k)
                    if ws >= k:
                        temp.append(char)
                        break
                    else:
                        k -= ws
                        hf[char] += 1 
        res = "".join(temp)
        return res + mid + res[::-1]