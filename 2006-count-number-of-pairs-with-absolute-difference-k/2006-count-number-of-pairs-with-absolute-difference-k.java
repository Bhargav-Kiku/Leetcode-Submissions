class Solution {
    public int countKDifference(int[] nums, int k) {
        Map<Integer, Integer> f = new TreeMap<>();
        for (int x: nums) {
            f.put(x, f.getOrDefault(x,0) + 1);
        }
        int res = 0;
        for (int x: nums) {
            res += f.getOrDefault(x+k,0);
        }
        return res;
    }
}