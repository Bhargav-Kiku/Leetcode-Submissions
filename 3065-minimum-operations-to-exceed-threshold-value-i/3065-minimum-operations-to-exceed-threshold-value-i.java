class Solution {
    public int minOperations(int[] nums, int k) {
        int res = 0;
        for (int x: nums) {
            if (x < k) res++;
        }
        return res;
    }
}