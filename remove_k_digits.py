# https://leetcode.com/problems/remove-k-digits/
# 402
# Medium

from itertools import permutations


num = "10200"
k = 1


def removeKdigits(num, k):
    res = int(num)
    i = 0
    if len(num) == k:
        res = 0
    else:
        while i+k <= len(num):
            # st = num[i:i+k]
            s = num[:i] + num[i+k:]
            if int(s) < res:
                res = int(s)
            i += 1

    return res


def removeKdigits2(num, k):
    # create an array of k nums from range(num)
    res = int(num)
    if len(num) == k:
        res = 0
    else:
        for choices in list(permutations(range(len(num)), k)):
            N = list(num)
            L = list(choices)
            L.sort(reverse=True, key=int)
            for i in L:
                # print(i)
                N.pop(i)

            N = ''.join(N)
            if int(N) > 0 and int(N) < res:
                res = int(N)
            elif int(N) == 0:
                res = 0
                break

    return res


def removeKdigits3(num, k):
    res = ""
    i = 0
    k = len(num) - k
    while i < len(num):
        if any(int(N) < int(num[i]) for N in num[i+1:]) \
                and len(num[i+1:]) >= k:
            i += 1
        else:
            res += num[i]
            k -= 1
            i += 1

    return res


# Using stack --- if the previous number is greater than the current
def removeKdigits4(num, k):
    K = len(num)

    if K == k:
        return "0"
    elif k == 0:
        return num

    S = []
    i = 0

    while i < K:
        n = int(num[i])
        if not S or k == 0:
            S.append(num[i])
        else:
            while (k > 0) and S and (n < int(S[-1])):
                S.pop()
                k -= 1
            S.append(num[i])
        i += 1

    while S and k > 0:
        S.pop()
        k -= 1

    ans = "".join(S)
    return str(int(ans))


x = removeKdigits3(num, k)
print(x)
