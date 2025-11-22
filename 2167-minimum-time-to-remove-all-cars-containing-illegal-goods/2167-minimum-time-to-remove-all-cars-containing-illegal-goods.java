class Solution {
    public int minimumTime(String s) {
        int c = 0;
        int x = 0;
        for (char i: s.toCharArray()) {
            if (i == '1') {
                c++;
            } else {
                c--;
            }
            if (c < x) {
                x = c;
            }
            if (c > 0) {
                c = 0;
            }
        }
        // System.out.print(x);
        return s.length() + x;
    }
}