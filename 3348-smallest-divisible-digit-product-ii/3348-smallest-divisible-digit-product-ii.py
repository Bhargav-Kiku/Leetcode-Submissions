class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tp = t
        for i in range(2, 10):
            while tp % i == 0:
                tp //= i
        if tp > 1:
            return "-1"
        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1
        nl = list(num)
        for i in range(n):
            if nl[i] == "0":
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(nl[i]))
        if rem[n] == 1:
            return num
        for i in range(pos, -1, -1):
            while True:
                nl[i] = chr(ord(nl[i]) + 1)
                if nl[i] > "9":
                    break
                tn = rem[i] // math.gcd(rem[i], int(nl[i]))
                k = 9
                for j in range(n - 1, i, -1):
                    while tn % k != 0:
                        k -= 1
                    tn //= k
                    nl[j] = str(k)
                if tn == 1:
                    return "".join(nl)
        res = []
        ot = t
        for i in range(9, 1, -1):
            while ot % i == 0:
                res.append(str(i))
                ot //= i
        ress = "".join(res)
        padding = max(n + 1 - len(ress), 0)
        ress += "1" * padding
        return ress[::-1]