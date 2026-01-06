class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        float res = (float)(nums[0] + nums[n-1]) / 2;
        for (int i = 1; i < n/2; i++)
            res = Math.min(res, (float)(nums[i] + nums[n-i-1]) / 2);
        return res;
    }
}