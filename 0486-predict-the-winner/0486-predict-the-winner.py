class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def sum(i,j):
            if i == j:
                return nums[i]
            sum1 = nums[i] - sum(i+1,j)
            sum2 = nums[j] - sum(i,j-1)
            return max(sum1, sum2)
        return sum(0,len(nums)-1) >= 0