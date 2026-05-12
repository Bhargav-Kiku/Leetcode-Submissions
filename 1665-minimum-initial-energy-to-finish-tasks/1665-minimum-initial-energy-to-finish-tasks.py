class Solution:
    def minimumEffort(self, shop: List[List[int]]) -> int:
        shop.sort(key=lambda x: x[1] - x[0], reverse=True)
        s = shop[0][1]
        c = shop[0][1] - shop[0][0]
        l = 0
        for i in range(1, len(shop)):
            ct, over = shop[i]
            if c < over:
                l += over - c
                c = over
            c -= ct
        return s + l