class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x:(x[0], -x[1]))
        ans = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            w, h = envelopes[i]
            if h > ans[-1]:
                ans.append(h)
            else:
                idx = bisect_left(ans, h)
                ans[idx] = h
        return len(ans)