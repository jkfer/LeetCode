import re

s = "3[a2[c]]"


def decodeString3(s):
    patt = re.compile(r'([0-9]+)\[([a-zA-Z]+)\]')

    while '[' in s:
        match = re.search(patt, s)
        new_s = int(match.group(1)) * str(match.group(2))
        s = s.replace(str(match.group(0)), new_s)
    
    return s



def decodeString(s):
    i = 0

    num_stack = []
    string_stack = []
    brack_stack = []
    res = ''

    
    for i, char in enumerate(s):
        if char.isdigit():
            num_stack.append(char)

        elif char == '[':
            if brack_stack == []:
                brack_stack.append(char)

            

        elif char.isalpha():
            string_stack.append(char)
        
        elif char == ']':
            print(num_stack, string_stack)
            res += int(''.join(num_stack)) * (''.join(string_stack))
            string_stack = []
            num_stack = []


        i += 1

    print(res)



def decodeString2(s):
    stack = []
    i = 0

    while i<len(s):

        if s[i].isdigit():
            num = ""
            while s[i]!="[":
                num = num + s[i]
                i += 1
            stack.append(num)

        elif s[i].isalpha() or s[i]=="[":
            stack.append(s[i])
            i += 1

        else: # s[i] == "]"
            pop = ""
            while stack[-1]!="[":
                pop = stack.pop() + pop
            stack.pop() 
            k = int(stack.pop())
            res = ""
            for _ in range(k):
                res = res + pop
            stack.append(res)
            i += 1

    final = ""
    while stack:
        final = stack.pop() + final

    return final


x = decodeString3(s)
print(x)





