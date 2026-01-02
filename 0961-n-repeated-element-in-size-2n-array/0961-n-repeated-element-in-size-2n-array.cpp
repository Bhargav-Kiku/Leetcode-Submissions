class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        set<int> s;;
        for (int x: nums) {
            if (s.count(x)) return x;
            s.insert(x);
        }
        return 0;
    }
};