class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n <= 2:
            return False
        def back(idx, l, ll):
            # print(idx,l,ll)
            if idx == n:
                print(idx,l,ll)
                return True
            if idx == 0:
                if num[idx] == '0':
                    return back(idx+1,0,l)
                c = 0
                for i in range(idx,n-2):
                    c = c * 10 + int(num[i])
                    x = back(i+1,c,l)
                    if x:
                        return True
            elif ll == -1:
                if num[idx] == '0':
                    return back(idx+1,0,l)
                else:
                    c = 0
                    for i in range(idx,n-1):
                        c = c * 10 + int(num[i])
                        x = back(i+1,c,l)
                        if x:
                            return True
            else:
                if num[idx] == '0':
                    if l + ll == 0:
                        return back(idx+1,0,l)
                    else:
                        return False
                c = 0
                for i in range(idx,n):
                    c = c * 10 + int(num[i])
                    if c == l + ll:
                        x = back(i+1,c,l)
                        if x:
                            return True
                    elif c > l + ll:
                        return False
            return False
                    
                
        return back(0,-1,-1)