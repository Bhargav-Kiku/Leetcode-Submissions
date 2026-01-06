class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        vector<int> ch(101);
        for (int x: nums) {
            ch[x] += 1;
        }
        int res = 0;
        for (int x: nums) {
            if (x + k < 101) {
                res += ch[x+k];
            }
        }
        return res;
    }
};