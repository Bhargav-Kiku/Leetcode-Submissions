class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        n = label
        i = 1
        while (i << 1) <= n:
            i <<= 1
        d = n - i
        return self.pathInZigZagTree(i - (d // 2 + 1)) + [label]