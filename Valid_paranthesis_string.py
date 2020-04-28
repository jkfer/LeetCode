# https://leetcode.com/problems/valid-parenthesis-string/
# 678


import collections


class Solution:
    def checkValidString(self, s):
        if len(s) == 0:
            return True

        st = []
        count = 0

        for n in s:
            if n == "(":
                st.append(n)
            elif n == ")":
                if st:
                    st.pop()
                else:
                    if count > 0:
                        count -= 1
                    else:
                        return False
            else:
                count += 1
                if st:
                    st.pop()
                    count += 1

        return st == []


S = Solution()
print(S.checkValidString("(*)"))
