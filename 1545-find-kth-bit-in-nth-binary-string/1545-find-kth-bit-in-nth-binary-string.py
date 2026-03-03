s = ["0"]
for _ in range(19):
    s = s + ["1"] + ["1" if x == "0" else "0" for x in s[::-1]]
print(s)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return s[k-1]