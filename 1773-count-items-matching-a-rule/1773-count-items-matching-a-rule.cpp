class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int res = 0;
        int toc = 0;
        if (ruleKey == "color") toc = 1;
        else if (ruleKey =="name") toc = 2;
        for (int i = 0; i < items.size(); i++) {
            if (items[i][toc] == ruleValue) res++;
        }
        return res;
    }
};