class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = []
        self.m = -1
        def check(i, path, on, cn):
            if i == len(s):
                if on == cn:
                    if len(path) == self.m:
                        self.res.append(path)
                    elif len(path) > self.m:
                        self.m = len(path)
                        self.res = [path]
                return
            if s[i] == '(':
                check(i+1,path+'(',on+1,cn)
                check(i+1,path,on,cn)
            elif s[i] == ')':
                if cn < on:
                    check(i+1,path+')',on,cn+1)
                check(i+1,path,on,cn)
            else:
                check(i+1,path+s[i],on,cn)
        check(0, "", 0, 0)
        return list(set(self.res))