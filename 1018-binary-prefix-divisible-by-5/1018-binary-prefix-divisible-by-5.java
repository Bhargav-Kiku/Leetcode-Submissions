class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        int n = 0;
        List<Boolean> res = new ArrayList();
        for (int x: nums) {
            n = (n * 2 + x) % 5;
            res.add(n==0);
        }
        return res;
    }
}