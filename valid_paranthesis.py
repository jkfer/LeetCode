
s = "(()"

def isValid(s):

    D = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    if len(s) % 2 == 0:
        res = True
        stack = []
        for char in s:
            if char in D:
                stack.append(char)
            else:
                if stack == []:
                    res = False
                else:
                    a = stack.pop()
                    if char != D[a]:
                        res = False
    else:
        res = False
    
    if stack != []:
        res = False

    return res

x = isValid(s)
print(x)