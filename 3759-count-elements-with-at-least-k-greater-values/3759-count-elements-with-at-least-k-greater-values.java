class Solution {
    public int countElements(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) return n;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i: nums) {
            map.put(i, map.getOrDefault(i,0) + 1);
        }
        List<Integer> ue = new ArrayList<>(map.keySet());
        Collections.sort(ue);

        int rm = n;
        int res = 0;

        for (int x: ue) {
            rm -= map.get(x);
            if (rm >= k) res += map.get(x);
            else break;
        }

        return res;
    }
}