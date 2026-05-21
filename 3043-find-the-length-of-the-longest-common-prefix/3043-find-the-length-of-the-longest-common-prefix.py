class Trie:
    def __init__(self):
        self.node = [None] * 10

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        head = Trie()
        for i in arr1:
            nn = head
            for j in str(i):
                if not nn.node[int(j)]:
                    nn.node[int(j)] = Trie()
                nn = nn.node[int(j)]
        res = 0
        for i in arr2:
            nn = head
            c = 0
            for j in str(i):
                if nn.node[int(j)]:
                    c += 1
                    nn = nn.node[int(j)]
                else:
                    break
            res = max(res, c)
        return res