class Solution {
public:
    int smallestRepunitDivByK(int k) {
        int n = 0, c = 0;
        if (k % 2 == 0 || k % 5 == 0) return -1;
        while (true) {
            n = (n * 10) + 1;
            n = n % k;
            c += 1;
            if (n == 0) return c;
        }
    }
};