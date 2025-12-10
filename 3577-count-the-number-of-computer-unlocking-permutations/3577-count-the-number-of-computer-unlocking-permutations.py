class Solution:
    def countPermutations(self, complexity: List[int]) -> int:    
        a = complexity
        c = 1
        v = len(a)-1
        s = a[0]
        for i in range(1,len(a)):
            if a[i] <= s:
                return 0
            c = (c * v) % (10**9 + 7)
            v -= 1
        return c