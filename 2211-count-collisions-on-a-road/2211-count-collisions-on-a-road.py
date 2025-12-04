class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        st = []
        for i in directions:
            if i == 'R':
                st.append(i)
            elif i == 'L':
                if st:
                    if st.pop() == 'R':
                        res += 2
                        while st and st[-1] == 'R':
                            res += 1
                            st.pop()
                    else:
                        res += 1
                    st.append('S')
            else:
                while st and st[-1] == 'R':
                    res += 1
                    st.pop()
                st.append(i)
            # print(res)
        return res