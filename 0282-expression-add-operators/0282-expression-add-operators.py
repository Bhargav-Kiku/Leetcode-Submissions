class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def dfs(i, path, cn, pn):
            if i == n:
                if cn == target:
                    res.append(path)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                sn = int(num[i:j+1])
                if i == 0:
                    dfs(j+1, path + str(sn), cn + sn, sn)
                else:
                    dfs(j+1, path + "+" + str(sn), cn + sn, sn)
                    dfs(j+1, path + "-" + str(sn), cn - sn, -sn)
                    dfs(j+1, path + "*" + str(sn), cn - pn + pn * sn, pn * sn)
        dfs(0,"",0,0)
        return res