class Solution {
    public int countKDifference(int[] nums, int k) {
        HashMap<Integer, Integer> f = new HashMap<>();
        for (int x: nums) {
            f.put(x, f.getOrDefault(x,0) + 1);
        }
        int res = 0;
        for (int x: nums) {
            if (f.containsKey(x+k)) {
                res += f.get(x+k);
            }
        }
        return res;
    }
}