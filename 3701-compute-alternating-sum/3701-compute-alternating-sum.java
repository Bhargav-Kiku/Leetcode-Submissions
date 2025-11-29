class Solution {
    public int alternatingSum(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((i & 1) == 0) {
                res += nums[i];
            } else {
                res -= nums[i];
            }
        }
        return res;
    }
}