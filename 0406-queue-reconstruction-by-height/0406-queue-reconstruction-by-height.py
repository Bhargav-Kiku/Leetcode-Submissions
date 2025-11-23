class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key = lambda x: (-x[0],x[1]))
        for a in people:
            res.insert(a[1],a)
        return res