class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        st = []

        for c in s:
            if c != "#":
                ss.append(c)
            else:
                if len(ss) > 0:
                    ss.pop()

        for c in t:
            if c != "#":
                st.append(c)
            else:
                if len(st) > 0:
                    st.pop()

        return ''.join(ss) == ''.join(st)