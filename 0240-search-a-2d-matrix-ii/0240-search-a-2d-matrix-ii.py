class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l = n - 1
        i = 0
        while l > -1 and i < m:
            s = 0
            while s <= l:
                mid = s + (l - s) // 2
                if matrix[mid][i] == target:
                    return True
                if matrix[mid][i] > target:
                    l = mid - 1
                else:
                    s = mid + 1
            i += 1
        return False