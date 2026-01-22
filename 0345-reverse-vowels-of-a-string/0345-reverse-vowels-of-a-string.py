vows = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        i = 0
        j = len(l) - 1
        while i < j:
            while i < j and s[i] not in vows:
                i += 1
            while j > i and s[j] not in vows:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return "".join(l)