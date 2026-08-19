class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(int)
        for x, y in reservedSeats:
            seats[x] |= 1 << (y - 1)
        res = (n - len(seats)) * 2
        rn = ((1 << 5) - 2)
        # print(bin(rn))
        for x in seats.values():
            f = False
            if x & (rn) == 0:
                f = True
                res += 1
            if x & (rn << 4) == 0:
                res += 1
                f = True
            if not f and x & (rn << 2) == 0:
                res += 1
        return res