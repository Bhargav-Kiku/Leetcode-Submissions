class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int n = 0;
        vector<bool> res;
        for (int x: nums) {
            n = (n * 2 + x) % 5;
            res.push_back(n==0);
        }
        return res;
    }
};