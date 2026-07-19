class Solution:
    def smallestSubsequence(self, s: str) -> str:
        mapy = {}
        for i, ch in enumerate(s):
            mapy[ch] = i
        st = []
        tk = set()
        for i, ch in enumerate(s):
            if ch in tk:
                continue
            while (st and
                   st[-1] > ch and
                   mapy[st[-1]] > i):
                tk.remove(st.pop())
            st.append(ch)
            tk.add(ch)
        return "".join(st)