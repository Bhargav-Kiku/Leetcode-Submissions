vs = {'a','b','c'}
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def recur(idx,s):
            # print(idx)
            if idx == n:
                res.append(s)
                return
            if idx == 0:
                for x in vs:
                    recur(1,x)
            else:
                for x in vs:
                    if x != s[-1]:
                        recur(idx+1,s+x)
        recur(0,"")
        # print(res)
        res.sort()
        if len(res) < k: return ""
        return res[k-1]