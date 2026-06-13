class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for w in words:
            c = 0
            for x in w:
                c += weights[ord(x) - 97]
            c %= 26
            # print(c)
            res.append(chr(97+25-c))
        return ''.join(res)