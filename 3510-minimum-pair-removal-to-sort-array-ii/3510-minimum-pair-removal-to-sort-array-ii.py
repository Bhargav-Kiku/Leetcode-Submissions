class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        L = list(range(-1, n - 1))
        R = list(range(1, n + 1))
        self.invs = sum(nums[i] > nums[i+1] for i in range(n-1))
        s = SortedList([nums[i] + nums[i+1], i] for i in range(n - 1))

        def add(x):
            y = R[x]
            if 0 <= x < y < n:
                s.add([nums[x] + nums[y], x])
                self.invs += nums[x] > nums[y]

        def remove(x):
            y = R[x]
            if 0 <= x < y < n:
                s.discard([nums[x] + nums[y], x])
                self.invs -= nums[x] > nums[y]
        
        res = 0
        while self.invs:
            res += 1
            su, i = s.pop(0)
            j = R[i]
            h, k = L[i], R[j] 
            remove(h)
            remove(i)
            remove(j)
            nums[i] += nums[j]
            R[i] = k
            if k < n:
                L[k] = i
            add(h)
            add(i)
        return res