class Solution {
    public int countElements(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) return n;
        Arrays.sort(nums);

        int idx = n - k - 1;

        while (idx >= 0 && nums[idx] == nums[idx+1]) {
            idx --;
        }

        return idx + 1;
    }
}