class Solution {
private:
    int MOD = 1000000007;
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        if (n == 1 || m == 1) {
            int ts = 0;
            for (auto& row: grid) {
                for (int x: row) {
                    ts += x;
                }
            }
            return (ts % k == 0) ? 1 : 0;
        }
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(k, 0)));;
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) continue;
                int v = grid[i][j] % k;
                for (int q = 0; q < k; q++) {
                    int r = (q + v) % k;
                    int res = 0;
                    if (i > 0) {
                        res += dp[i-1][j][q];
                    }
                    if (j > 0) {
                        res += dp[i][j-1][q];
                    }
                    dp[i][j][r] = (dp[i][j][r] + res) % MOD;
                }
            }
        }
        return dp[n-1][m-1][0];
    }
};