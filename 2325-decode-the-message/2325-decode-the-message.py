class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        maps = {' ': ' '}
        t = ord('a')
        for i in key:
            if i not in maps:
                maps[i] = chr(t)
                t += 1
        res = ""
        for i in message:
            res += maps[i]
        return res