class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        n = len(word)
        while i < n:
            if word[i] == ch:
                break
            i += 1
        if i == n:
            return word
        return word[:i+1][::-1] + word[i+1:]