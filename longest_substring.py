#!/usr/bin/python

# find the length of the longest substring with unique charachters of a given string:

#s = ''
s = 'aajakubj'

def lengthOfLongestSubstring(s):
    le = 0
    re = ""
    i = 0
    while i < len(s):
        if re == "" and i+1 < len(s):
            poin = i + 1
        if s[i] not in re:
            re += s[i]
            i += 1
            #le = len(re)
        else:
            if len(re) > le:
                le = len(re)
            re = ""
            i = poin
    if len(re) > le:
        return len(re)
    else:
        return le

# re-coding this better with sliding window option:
def lengthOfLongestSubstring2(s):
    # initiate a list:
    res = []
    m = 0
    for i in range(len(s)):
        if s[i] not in res:
            res.append(s[i])
        else:
            j = res.index(s[i])
            res = res[j+1:]
            res.append(s[i])
        m = max(m, len(res))
    return m


    

x = lengthOfLongestSubstring2('abcabcbb')
print(x)
