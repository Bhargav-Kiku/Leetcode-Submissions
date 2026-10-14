class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9 < sum:
            return ""
        res = '9' * (sum // 9) + (str(sum % 9) if sum % 9 else "")
        return res + ('0' * (num - len(res)))