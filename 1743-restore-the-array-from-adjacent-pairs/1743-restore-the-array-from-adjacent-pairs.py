class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mps = {}
        for i, j in adjacentPairs:
            if i not in mps:
                mps[i] = []
            mps[i].append(j)
            if j not in mps:
                mps[j] = []
            mps[j].append(i)
        res = []
        vis = set()
        for i, j in mps.items():
            if len(j) == 1:
                res.append(i)
                vis.add(i)
                break
        while len(res) < len(mps):
            for x in mps[res[-1]]:
                if x not in vis:
                    vis.add(x)
                    res.append(x)
        return res