class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((8 * n) ** (0.5)) // 2