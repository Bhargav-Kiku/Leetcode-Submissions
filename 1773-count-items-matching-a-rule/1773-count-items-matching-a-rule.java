class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int res = 0;
        int toc = 0;
        if (ruleKey.equals("color")) toc = 1;
        else if (ruleKey.equals("name")) toc = 2;
        for (List<String> pair: items) {
            if (pair.get(toc).equals(ruleValue)) {
                res += 1;
            }
        }
        return res;
    }
}