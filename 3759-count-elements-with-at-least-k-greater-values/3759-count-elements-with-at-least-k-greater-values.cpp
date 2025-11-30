class Solution {
public:
    int countElements(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 0) return n;
        sort(nums.begin(), nums.end());
        
        int idx = n - k - 1;

        while (idx >= 0 && nums[idx] == nums[idx+1]) {
            idx--;
        }

        return idx+1;
    }
};