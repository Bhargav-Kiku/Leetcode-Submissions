class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        arr = [0] * 26
        n = len(s)
        for i in range(n):
            arr[ord(s[i]) - ord('a')] = i
        for i in range(n):
            arr[ord(t[i]) - ord('a')] -= i
        res = 0
        for i in arr:
            res += abs(i)
        return res