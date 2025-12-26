class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        res = 0
        mm = 0
        tem = 0
        for i in range(n):
            if customers[i] == 'Y':
                tem += 1
            else:
                tem -= 1
            if tem > mm:
                mm = tem
                res = i + 1
        return res