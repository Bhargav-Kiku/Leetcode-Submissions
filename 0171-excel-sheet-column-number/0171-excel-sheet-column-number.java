class Solution {
    public int titleToNumber(String columnTitle) {
        int res = 0;
        int g = (int) 'A';
        for (char c: columnTitle.toCharArray()) {
            res = (res * 26) + ((int) c - g + 1);
        }
        return res;
    }
}