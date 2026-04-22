class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        n = len(queries[0])
        for q in queries:
            for d in dictionary:
                c = 0
                for i in range(n):
                    if q[i] != d[i]:
                        c += 1
                    if c > 2:
                        break
                if c <= 2:
                    res.append(q)
                    break
        return res