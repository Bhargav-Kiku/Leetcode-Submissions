class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int n = nums.size();
        int xo = 0;
        vector<int> res (n, 0);
        for (int x: nums) {
            xo ^= x;
        }
        int me = (1 << maximumBit) - 1;
        for (int i = n-1; i >= 0; i --) {
            res[n-i-1] = (me ^ xo);
            xo ^= nums[i];
        }
        return res;
    }
};