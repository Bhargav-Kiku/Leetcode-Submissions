class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int res = 0;
        int toc = 0;
        if (ruleKey == "color") toc = 1;
        else if (ruleKey =="name") toc = 2;
        for (vector<string> pair: items) {
            if (pair[toc] == ruleValue) {
                res += 1;
            }
        }
        return res;
    }
};