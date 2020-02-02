

# longest palindromic substring

s = "abbba"
# s = "babad"
# s = ""
# s = "aa"
# s = "ac"
# s = "a"


def longest(s):
    i = 0
    re = ""
    word = ""
    while s[i:] != '':
        beg = s[i]
        rem = s[i+1:]
        word = s[i]
        while beg in rem:
            x = rem.index(beg)
            word = word + rem[:x+1]
            if word == word[::-1] and len(word) > len(re):
                re = word
            rem = rem[x+1:]
        i += 1
    if re == "" and s != "":
        re = s[0]

    return re


ans = longest(s)
print(ans)
