class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        setA = set()
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                setA.add(hFences[j] - hFences[i])
        res = -1
        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                v = (vFences[j] - vFences[i])
                if v in setA:
                    res = max(res,v)
        return (res ** 2) % (1000000007) if res != -1 else -1