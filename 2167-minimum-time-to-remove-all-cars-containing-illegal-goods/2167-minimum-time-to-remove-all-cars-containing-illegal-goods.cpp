class Solution {
public:
    int minimumTime(string s) {
        int c = 0;
        int x = 0;
        for (char i: s) {
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
        return s.length() + x;
    }
};