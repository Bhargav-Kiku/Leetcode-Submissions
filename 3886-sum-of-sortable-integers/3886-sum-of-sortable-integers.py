class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        have = ''.join(map(chr, nums))
        want = ''.join(sorted(have))
        def sortable(k):
            return n % k == 0 and all(
                have[i:i+k] in want[i:i+k] * 2
                for i in range(0, n, k)
            )
        return sum(filter(sortable, range(1, n+1)))