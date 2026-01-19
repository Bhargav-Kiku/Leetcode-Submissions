class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n,p = len(mat),len(mat[0]),[*zip(*map(accumulate,zip(*map(accumulate,mat))))]
        check = lambda q: all(p[i][j]-(i>=q and p[i-q][j])-(j>=q and p[i][j-q])+
            (i>=q<=j and p[i-q][j-q])>threshold for i,j in product(range(q-1,m),range(q-1,n)))
        return bisect_left(range(1,min(m,n)+1),1,key=check)