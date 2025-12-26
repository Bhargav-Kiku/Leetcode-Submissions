class Solution:
    def check(self,maps,k):
        for x in maps.values():
            if x < k:
                return False
        return True
    def longestSubstring(self, s: str, k: int) -> int:
        # print(s)
        c = Counter(s)
        if self.check(c,k):
            return len(s)
        temp = ''
        res = 0
        for i in s:
            if c[i] < k:
                res = max(res, self.longestSubstring(temp,k))
                temp = ''
            else:
                temp += i
        res = max(res, self.longestSubstring(temp,k))
        return res