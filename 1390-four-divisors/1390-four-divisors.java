class Solution {
    private static HashMap<Integer,Set<Integer>> map = new HashMap<>();
    static {
        for (int i = 1; i <= 100000; i++) {
            Set<Integer> set = new HashSet<>();
            for (int j = 1; j * j <= i; j++) {
                if (i % j == 0) {
                    set.add(j);
                    set.add(i/j);
                    if (set.size() > 4) break;
                }
            }
            if (set.size() == 4) {
                map.put(i,set);
            }
        }
    }

    public int sumFourDivisors(int[] nums) {
        int res = 0;
        for (int x: nums) {
            if (map.containsKey(x)) {
                for (int y: map.get(x)) {
                    res += y;
                }
            }
        }
        return res;
    }
}