class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n+1,0);
        for (int i = 0; i < n; i++) {
            int cs = 0;
            int cm = 0;
            for (int j = i; j > max(-1, i - k); j--) {
                if (cm < arr[j]) cm = arr[j];
                int cur = cm * (i - j + 1) + dp[j];
                if (cur > cs) cs = cur;
            }
            dp[i+1] = cs;
        }
        return dp[n];
    }
};