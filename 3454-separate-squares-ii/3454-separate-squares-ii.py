class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        ets = []
        for x, y, length in squares:
            ets.append((y, 1, x, x + length))
            ets.append((y + length, -1, x, x + length))

        ets.sort()

        ai = []  
        py = ets[0][0]
        ta = 0
        hs = [] 

        def union_width(intervals):
            intervals.sort()
            tw = 0
            rim = -10**30
            for left, right in intervals:
                if left > rim:
                    tw += right - left
                    rim = right
                elif right > rim:
                    tw += right - rim
                    rim = right
            return tw

        for y, et, x_left, x_right in ets:
            if y > py and ai:
                height = y - py
                width = union_width(ai)
                hs.append((py, height, width))
                ta += height * width

            if et == 1:
                ai.append((x_left, x_right))
            else:
                ai.remove((x_left, x_right))

            py = y

        ha = ta / 2
        aa = 0

        for sy, height, width in hs:
            sa = height * width
            if aa + sa >= ha:
                return sy + (ha - aa) / width
            aa += sa

        return float(py)
