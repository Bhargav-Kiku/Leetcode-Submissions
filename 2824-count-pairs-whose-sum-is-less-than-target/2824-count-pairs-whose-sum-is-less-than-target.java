class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int n = nums.size();
        int res = 0;
        Collections.sort(nums);
        for (int i = 0; i < n; i++) {
            int x = nums.get(i);
            for (int j = i + 1; j < n; j++) {
                if (x + nums.get(j) < target) res++;
                else break;
            }
        }
        return res;
    }
}