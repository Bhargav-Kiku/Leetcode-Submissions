class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    @lru_cache(None)
    def dfs(ring: str, idx: int) -> int:
      if idx == len(key):
        return 0
      ans = float('inf')
      for i, r in enumerate(ring):
        if r == key[idx]:
          mr = min(i, len(ring) - i)
          nr = ring[i:] + ring[:i]
          remr = dfs(nr, idx + 1)
          ans = min(ans, mr + remr)

      return ans

    return dfs(ring, 0) + len(key)