class Solution {
    public int countCollisions(String directions) {
        int lc = 0;
        int rc = 0;
        int sc = 0;
        int n = directions.length();
        for (int i = 0; i < n; i++) {
            if (directions.charAt(i) == 'L') lc ++;
            else break;
        }
        for (int i = n - 1; i > -1; i--) {
            if (directions.charAt(i) == 'R') rc ++;
            else break;
        }
        for (int i = n - 1; i > -1; i--) {
            if (directions.charAt(i) == 'S') sc ++;
        }
        return n - lc - rc - sc;
    }
}