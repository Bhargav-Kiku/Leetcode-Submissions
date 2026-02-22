fs = {
    1: [],
    2: [2],
    3: [3],
    4: [2, 2],
    5: [5],
    6: [2, 3]
}
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        self.cnt = [0] * 6
        while k > 1:
            if k % 2 == 0:
                self.cnt[2] += 1
                k //= 2
            elif k % 3 == 0:
                self.cnt[3] += 1
                k //= 3
            elif k % 5 == 0:
                self.cnt[5] += 1
                k //= 5
            else:
                return 0
        # self.res = 0
        n = len(nums)
        memo = {}
        def back(i, cnt):
            key = (i, '#'.join(map(str, cnt)))
            if key in memo:
                return memo[key]
            if i == n:
                # print(cnt)
                if cnt == self.cnt:
                    # self.res += 1
                    return 1
                return 0
            t = back(i+1, cnt)
            nc = cnt[:]
            nc2 = cnt[:]
            for x in fs[nums[i]]:
                nc[x] -= 1
                nc2[x] += 1
            memo[key] = t + back(i+1, nc) + back(i+1, nc2)
            return memo[key]

        return back(0, [0] * 6)
        # return self.res