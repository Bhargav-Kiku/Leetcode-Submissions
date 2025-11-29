class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (int x: nums) {
            if (!set.insert(x).second) return true;
        }
        return false;
    }
};