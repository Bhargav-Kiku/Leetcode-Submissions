class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        d = 1
        for i in preorder.split(','):
            d -= 1
            if d < 0:
                return False
            if i != '#':
                d += 2
        return d == 0