# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s):
        ANS = ""
        i = 0
        while i < len(s):
            if s[i] != " ":
                word = ""
                while i < len(s) and s[i] != " ":
                    word += s[i]
                    i += 1

                if ANS == "":
                    ANS = word
                else:
                    ANS = word + " " + ANS
            else:
                i += 1

        return ANS


s = "  hello world!  "
S = Solution()
print(S.reverseWords(s))
