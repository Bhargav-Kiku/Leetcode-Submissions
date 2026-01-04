class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if i == k or j == k: continue
                    for l in range(n):
                        if i == l or j == l or k == l: continue
                        if words[i][0] == words[j][0] and words[i][3] == words[k][0] and words[l][0] == words[j][3] and words[l][3] == words[k][3]:
                            res.append((words[i],words[j],words[k],words[l]))
        return sorted(res)