class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ca = [0] * 26
        n = len(s)
        res = []
        for i in range(n//2):
            res.append(s[i])
        res.sort()
        temp = res[::-1]
        if n % 2:
            res.append(s[n//2])
        res.extend(temp)
        return ''.join(res)