class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = True
        for i in range(n-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                c = False
                break
        if c: return [1] + digits
        return digits