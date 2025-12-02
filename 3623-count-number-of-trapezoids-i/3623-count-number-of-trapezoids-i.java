class Solution {
    private int MOD = 1000000007;
    public int countTrapezoids(int[][] points) {
        int res = 0;
        Map<Integer, Integer> m = new HashMap<>();
        for (int[] pair: points) {
            m.put(pair[1],m.getOrDefault(pair[1],0)+1);
        }
        List<Long> li = m.values().stream().filter(x -> x >= 2).map(x -> ((long)x * (x - 1) / 2)).collect(Collectors.toList());
        long tot = 0;
        for (Long x: li) tot = (tot + x) % MOD;
        for (Long x: li) {
            tot = (tot - x + MOD) % MOD;
            res = (int)(res + (tot * x) % MOD) % MOD;
        }
        return res;
    }
}