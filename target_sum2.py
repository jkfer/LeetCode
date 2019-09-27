
s = [2, 3, 8, 11, 16, 8, 5, 9, 7]
target = 16

# get all the combination of numbers from the list that add up to the target

def check_sum(s, target, partial=[]):
    S = sum(partial)

    if S == target:
        print(partial)
    if S >= target:
        return

    for i in range(len(s)):
        n = s[i]
        remaining = s[i+1:]
        check_sum(remaining, target, partial + [n])
    

check_sum(s, target)
#print(x)

