class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[1],b[1]));
        int n = pairs.length;
        int l = 1;
        int end = pairs[0][1];
        for (int i = 1; i < n; i++) {
            if (end < pairs[i][0]) {
                l += 1;
                end = pairs[i][1];
            }
        }
        return l;
    }
}