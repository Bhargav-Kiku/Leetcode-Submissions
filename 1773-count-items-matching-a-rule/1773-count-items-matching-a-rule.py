class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        toc = 0
        if ruleKey == "color":
            toc = 1
        elif ruleKey == "name":
            toc = 2
        for i in items:
            if i[toc] == ruleValue:
                res += 1
        return res