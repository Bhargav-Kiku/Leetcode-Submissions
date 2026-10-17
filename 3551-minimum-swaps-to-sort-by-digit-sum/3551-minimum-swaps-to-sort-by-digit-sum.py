def su(n):
    return sum(list(map(int, str(n))))
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            nums[i] = (i,su(num),num)
            
        s_nums = sorted(nums, key = lambda x:(x[1],x[2]))
        
        i_map = {s_nums[i][0]: i for i in range(n)}
        
        dp = [False] * n
        c = 0
        for i in range(n):
            if dp[i] or i_map[i] == i:
                continue
            c_len = 0
            j = i
            while not dp[j]:
                dp[j] = True
                j = i_map[j]
                c_len += 1
            if c_len > 1:
                c += c_len - 1
        return c