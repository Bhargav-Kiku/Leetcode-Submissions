class Solution {
    public int maximumWealth(int[][] accounts) {
        int res = 0;
        for (int i = 0; i < accounts.length; i++) {
            int s = 0;
            for (int x: accounts[i]) s += x;
            if (s > res) res = s;
        }
        return res;
    }
}