class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        j = 0
        c = 0
        for r in range(k - 1, len(s)):
            l = r - k + 1
            if (l >= j and check(s, l, r)) or (l > j and check(s, l-1, r)):
                c += 1
                j = r + 1
        return c