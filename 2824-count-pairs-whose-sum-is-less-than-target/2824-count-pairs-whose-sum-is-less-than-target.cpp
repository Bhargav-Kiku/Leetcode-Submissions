class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int res = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] < target) res++;
                else break;
            }
        }
        return res;
    }
};