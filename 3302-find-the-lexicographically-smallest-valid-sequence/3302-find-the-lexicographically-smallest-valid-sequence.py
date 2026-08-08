class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        lo = [-1] * m
        j = m - 1
        for i in range(n-1, -1, -1):
            if j == -1: break
            if word1[i] == word2[j]:
                lo[j] = i
                j -= 1
        res = []
        rem = True
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif rem and (j == m - 1 or i < lo[j + 1]):
                rem = False
                res.append(i)
                j += 1
        if j == m:
            return res
        return []