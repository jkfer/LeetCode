# https://leetcode.com/problems/string-compression/
# 443


class Solution:
    # gives only the final length - not the modified array
    def compress(self, chars):
        S = []
        new = []
        for i, char in enumerate(chars):
            if not S or (S[-1] == char):
                S.append(char)
            else:
                new.append(S[0])
                if len(S) > 1:
                    new.append(str(len(S)))
                S = [char]

        if len(S) > 1:
            new += [S[0], str(len(S))]
        else:
            new += [S[0]]

        return len(new)

    # copied working solution - two pointer method
    def compress2(self, chars):
        walker, runner = 0, 0
        while runner < len(chars):

            chars[walker] = chars[runner]
            count = 1

            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1

            runner += 1
            walker += 1

        return walker


S = Solution()
print(S.compress(list('aaabbbghujkkk')))  # a3b3ghujk3
print(S.compress2(list('aaabbbghujkkk')))
