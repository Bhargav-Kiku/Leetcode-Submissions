class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int[] dp = new int[n+1];
        Arrays.fill(dp,0);
        for (int i = 0; i < n; i++) {
            int cs = 0;
            int cm = 0;
            for (int j = i; j > Math.max(-1, i - k); j--) {
                if (cm < arr[j]) cm = arr[j];
                int cur = cm * (i - j + 1) + dp[j];
                if (cur > cs) cs = cur;
            }
            dp[i+1] = cs;
        }
        return dp[n];
    }
}