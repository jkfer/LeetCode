

s = 'MCMXCIV'


def romanToInt(s):
    D1 = {
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4,
    }

    D2 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    value = 0
    for i in D1.keys():
        if i in s:
            x = s.index(i)
            s = s[:x] + s[x+2:]
            value += D1[i]
            #print(s)

    """
    if len(s) > 0:
        for j in D2.keys():
            if j in s:
                y = s.index(j)
                s = s[:y] + s[y+1:]
                value += D2[j]
    """

    if len(s) > 0:
        for lett in list(s):
            value += D2[lett]


    return value


x = romanToInt(s)
print(x)
