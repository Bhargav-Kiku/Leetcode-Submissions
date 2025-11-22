class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length;
        int m = matrix[0].length;
        int j = 0;
        int l = n - 1;
        while (j < m && l > -1) {
            int s = 0;
            while (s <= l) {
                int mid = (s + l) / 2;
                if (matrix[mid][j] == target) return true;
                if (matrix[mid][j] < target) s = mid + 1;
                else l = mid - 1;
            }
            j++;
        }
        return false;
    }
}