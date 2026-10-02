class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(s,no,nc):
            if len(s) == 2*n:
                res.append(s)
                return
            if no < n:
                gen(s+'(',no+1,nc)
            if nc < no:
                gen(s+')',no,nc+1)
        gen("",0,0)
        return res