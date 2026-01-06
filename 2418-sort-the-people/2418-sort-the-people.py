class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x for x, y in (sorted(zip(names,heights), key = lambda x: -x[1]))]