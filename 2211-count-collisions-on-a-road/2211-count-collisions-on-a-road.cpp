class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.length();
        int lc = 0;
        int rc = n;
        int sc = 0;
        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') lc ++;
            else break;
        }
        for (int i = n - 1; i > -1; i--) {
            if (directions[i] == 'R') rc --;
            else break;
        }
        for (int i = lc; i < rc ; i++) {
            if (directions[i] != 'S') sc ++;
        }
        return sc;
    }
};