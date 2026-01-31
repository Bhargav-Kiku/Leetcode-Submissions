class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        l = 0
        h = len(letters)
        res = letters[0]
        while l <= h:
            m = l + (h - l) // 2
            if letters[m] > target:
                h = m - 1
                res = letters[m]
            else:
                l = m + 1
        return res