class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int res = (nums[0] + nums[n-1]);
        for (int i = 1; i < n/2; i++)
            res = Math.min(res, (nums[i] + nums[n-i-1]));
        return (float)res/2;
    }
}