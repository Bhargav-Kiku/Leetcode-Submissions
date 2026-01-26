class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        res = []
        md = arr[1] - arr[0]
        for i in range(n-1):
            v = arr[i + 1] - arr[i]
            if v == md:
                res.append([arr[i],arr[i+1]])
            elif v < md:
                md = v
                res = [[arr[i],arr[i+1]]]
        return res