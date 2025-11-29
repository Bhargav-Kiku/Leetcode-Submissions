class Solution {
    public int countDigits(int num) {
        int cn = num;
        int res = 0;
        while (cn > 0) {
            if ((num % (cn % 10)) == 0) res++;
            cn /= 10;
        }
        return res;
    }
}