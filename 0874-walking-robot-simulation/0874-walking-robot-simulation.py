class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        o_s=set()
        for (x, y) in obstacles:
            o_s.add((x, y))
        dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y, dx, dy, f, md = 0, 0, 0, 1, 0, 0
        for  c in commands:
            if c == -2:
                f = (f+1)&3
                dx = dir[f][0]
                dy = dir[f][1]
            elif c == -1:
                f = (f+3)&3
                dx = dir[f][0]
                dy = dir[f][1]
            else:
                for i in range(c):
                    x += dx
                    y += dy
                    if (x, y) in o_s:
                        x -= dx
                        y -= dy
                        break
                md = max(md, x*x+y*y)
        return md
