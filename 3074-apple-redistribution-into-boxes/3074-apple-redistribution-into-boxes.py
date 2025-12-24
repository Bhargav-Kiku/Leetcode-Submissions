class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t = sum(apple)
        capacity.sort(reverse = True)
        res = 0
        for i in capacity:
            t -= i
            res += 1
            if t <= 0:
                break
        return res