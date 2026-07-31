class Solution {
    public void dfs(char[][] grid, int n, int m, int x, int y) {
        grid[x][y] = '0';
        if (x > 0 && grid[x-1][y] == '1') {
            dfs(grid, n, m, x-1, y);
        }
        if (x+1 < n && grid[x+1][y] == '1') {
            dfs(grid, n, m, x+1, y);
        }
        if (y > 0 && grid[x][y-1] == '1') {
            dfs(grid, n, m, x, y-1);
        }
        if (y+1 < m && grid[x][y+1] == '1') {
            dfs(grid, n, m, x, y+1);
        }
    }
    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        // System.out.println(n + " " + m);
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    res += 1;
                    dfs(grid, n, m, i, j);
                }
            }
        }
        return res;
    }
}