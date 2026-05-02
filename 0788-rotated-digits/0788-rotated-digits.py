def check(x):
    f1 = False
    while x > 0:
        if x % 10 in {2, 5, 6, 9}:
            f1 = True
        x //= 10
    return f1

pre = [0] * (10001)
for i in range(2, 10001):
    pre[i] = pre[i-1]
    f = False
    for x in {'3', '4', '7'}:
        if x in str(i):
            f = True
            break
    if f: continue
    pre[i] += check(i)
# print(pre)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return pre[n]