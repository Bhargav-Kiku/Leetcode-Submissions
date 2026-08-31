class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCrit(x, y, z):
            return (y.val - x.val) * (y.val - z.val) > 0
        c = [0, 0]
        miv, i = inf, 1
        pv, cur, nxt = head, head.next, head.next.next        
        while nxt:
            if isCrit(pv, cur, nxt):
                if c[0]: miv = min(miv, i - c[c[1] > 0])
                c[c[0] > 0] = i
            pv, cur, nxt = cur, nxt, nxt.next
            i += 1
        return [[miv, c[1] - c[0]], [-1, -1]][not c[1]]