class Solution {
    public int balancedStringSplit(String s) {
        int c = 0;
        int res = 0;
        for (char x: s.toCharArray()) {
            if (x == 'L') {
                c ++;
            } else {
                c--;
            }
            if (c == 0) res++;
        }
        return res;
    }
}