from itertools import permutations

num = "10"
k = 2

def removeKdigits(num, k):
    res = int(num)
    i = 0
    if len(num) == k:
        res = 0
    else:
        while i+k <= len(num):
            #st = num[i:i+k]
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
                #print(i)
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
        if any(int(N) < int(num[i]) for N in num[i+1:]) and len(num[i+1:]) >= k:
            i += 1
        else:
            res += num[i]
            k -= 1
            i += 1
    
    return res


x = removeKdigits3(num, k)
print(x)