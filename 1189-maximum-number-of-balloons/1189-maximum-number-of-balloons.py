class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mapy = defaultdict(int)
        for i in text:
            mapy[i] += 1
        res = len(text)
        res = min(res, mapy['b'])
        res = min(res, mapy['a'])
        res = min(res, mapy['l']//2)
        res = min(res, mapy['o']//2)
        res = min(res, mapy['n'])
        return res