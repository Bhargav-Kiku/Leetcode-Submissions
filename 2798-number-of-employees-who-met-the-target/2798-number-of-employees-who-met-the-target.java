class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int res = 0;
        for (int x: hours) {
            if (x >= target) res++;
        }
        return res;
    }
}