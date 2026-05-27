class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = [0] * 26
        for i in word:
            if i.islower():
                if c[ord(i) - ord('a')] in [2, -1]:
                    c[ord(i) - ord('a')] = -1
                else:
                    c[ord(i) - ord('a')] = 1
            elif i.isupper():
                if c[ord(i) - ord('A')] == 0:
                    c[ord(i) - ord('A')] = -1
                elif c[ord(i) - ord('A')] == 1:
                    c[ord(i) - ord('A')] = 2
        # print(c)
        return sum(x == 2 for x in c)