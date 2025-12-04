class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.length();
        int lc = 0;
        int rc = n-1;
        int sc = 0;
        while (directions[lc] == 'L') {
            lc ++;
        }
        while (rc >= 0 && directions[rc] == 'R') {
            rc --;
        }
        for (int i = lc; i <= rc ; i++) {
            if (directions[i] != 'S') sc ++;
        }
        return sc;
    }
};