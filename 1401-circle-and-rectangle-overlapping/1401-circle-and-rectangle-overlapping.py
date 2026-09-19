class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cX = max(x1, min(xCenter, x2))
        cY = max(y1, min(yCenter, y2))
        dx = xCenter - cX
        dy = yCenter - cY
        return dx * dx + dy * dy <= radius * radius