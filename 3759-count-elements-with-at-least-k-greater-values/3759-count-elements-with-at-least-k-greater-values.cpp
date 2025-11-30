class Solution {
public:
    int countElements(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 0) return n;
        map<int, int> f;
        for (int i: nums) {
            f[i]++;
        }
        int rm = n;
        int res = 0;

        for (auto& pair : f) {
            int x = pair.first;
            int y = pair.second;
            rm -= y;
            if (rm >= k) res += y;
            else break;
        }

        return res;
    }
};