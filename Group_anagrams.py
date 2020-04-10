# https://leetcode.com/problems/group-anagrams
# 49


def groupAnagrams(self, strs):
    D = {}
    for word in strs:
        if "".join(sorted(word)) in D:
            D["".join(sorted(word))].append(word)
        else:
            D["".join(sorted(word))] = [word]

    ANS = []
    for key in D:
        ANS.append(D[key])

    return ANS
