class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        odr = sorted(range(n), key=lambda i: positions[i])
        h = healths[:]
        a = [True]*n
        st = []
        for i in odr:
            if directions[i] == 'R':
                st.append(i)
            else:
                while st:
                    t = st[-1]
                    if h[t] < h[i]:
                        a[t] = False
                        st.pop()
                        h[i] -= 1
                    elif h[t] > h[i]:
                        a[i] = False
                        h[t] -= 1
                        break
                    else:
                        a[t] = False
                        a[i] = False
                        st.pop()
                        break
        return [h[i] for i in range(n) if a[i]]