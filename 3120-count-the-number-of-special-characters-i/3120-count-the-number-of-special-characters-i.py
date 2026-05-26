class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = set()
        lm = set()
        cm = set()
        for i in word:
            if i.isupper():
                if i in cm:
                    res.add(i.lower())
                lm.add(i.lower())
            else:
                if i in lm:
                    res.add(i.lower())
                cm.add(i.upper())
        return len(res)