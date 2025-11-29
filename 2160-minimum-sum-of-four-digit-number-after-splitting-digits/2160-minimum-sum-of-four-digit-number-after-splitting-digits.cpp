class Solution {
public:
    int minimumSum(int num) {
        vector<int> s;
        while (num > 0) {
            s.push_back(num % 10);
            num /= 10;
        }
        sort(s.begin(), s.end());
        return s[0] * 10 + s[1] * 10 + s[2] + s[3]; 
    }
};