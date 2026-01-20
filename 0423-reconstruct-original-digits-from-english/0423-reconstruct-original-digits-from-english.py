class Solution:
    def getRes(self, f):
        maps = defaultdict(int)
        maps[0] = f['z']
        maps[2] = f['w']
        maps[4] = f['u']
        maps[6] = f['x']
        maps[8] = f['g']
        maps[1] = f['o'] - maps[0] - maps[2] - maps[4]
        maps[3] = f['h'] - maps[8]
        maps[5] = f['f'] - maps[4]
        maps[7] = f['s'] - maps[6]
        maps[9] = f['i'] - maps[5] - maps[6] - maps[8]
        return "".join(f'{i}' * maps[i] for i in range(10))

    def originalDigits(self, s: str) -> str:
        f = Counter(s)
        return self.getRes(f)