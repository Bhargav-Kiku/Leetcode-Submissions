class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = [None] * (4 * len(s))
        def merge(l, r):
            lc = l[0]
            rc = r[1]
            length = l[2] + r[2]
            best = max(l[5], r[5])
            pre = l[3]
            if l[3] == l[2] and l[1] == r[0]:
                pre = l[2] + r[3]
            suf = r[4]
            if r[4] == r[2] and l[1] == r[0]:
                suf = l[4] + r[2]
            if l[1] == r[0]:
                best = max(best, l[4] + r[3])
            return (lc, rc, length, pre, suf, best)
        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        build(1, 0, len(s) - 1)
        res = []
        for i in range(len(queryCharacters)):
            update(
                1,
                0,
                len(s) - 1,
                queryIndices[i],
                queryCharacters[i]
            )
            res.append(tree[1][5])
        return res