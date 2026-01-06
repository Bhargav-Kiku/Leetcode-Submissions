class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int res = (nums[0] + nums[n-1]);
        for (int i = 1; i < n/2; i++)
            res = min(res, (nums[i] + nums[n-i-1]));
        return (float)res/2;
    }
};