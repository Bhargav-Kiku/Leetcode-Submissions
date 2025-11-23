class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        m1 = []
        m2 = []
        t = 0
        for i in nums:
            t += i
            if i % 3 == 1:
                m1.append(i)
            elif i % 3 == 2:
                m2.append(i)
        if t % 3 == 0: return t
        m1.sort()
        m2.sort()
        rem = t % 3
        if rem == 1:
            op1 = t - m1[0] if len(m1) >= 1 else 0
            op2 = t - m2[0] - m2[1] if len(m2) >= 2 else 0
        elif rem == 2:
            op1 = t - m2[0] if len(m2) >= 1 else 0
            op2 = t - m1[0] - m1[1] if len(m1) >= 2 else 0
        return max(op1,op2)