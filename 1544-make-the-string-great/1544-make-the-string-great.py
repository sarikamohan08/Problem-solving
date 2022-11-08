class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if st:
                if i.isupper() and st[-1].islower() and st[-1].upper() == i: 
                    st.pop()
                    continue
                elif i.islower() and st[-1].isupper() and st[-1].lower() == i:
                    st.pop()
                    continue
                else:
                    st.append(i)
                    continue 
            else:
                st.append(i)
                continue
        return "".join(st)