from math import pow

def reverse(x):
    
    if x > 0:  # handle positive numbers  
        a =  int(str(x)[::-1])  
    if x <=0:  # handle negative numbers  
        a = -1 * int(str(x*-1)[::-1])  
    # handle 32 bit overflow  
    mina = -2**31  
    maxa = 2**31 - 1  
    if mina <= a <= maxa:  
        return a
    else:  
        return 0


def reverse2(x):
    """
    Concept is divide the integer by 0 until the answer is 0. Take the remainder each time and multiply it by 10s base and add it together
    """
    
    neg = True if x < 0 else False
    
    if x < 0:
        x = x * -1

    l = len(str(x).lstrip('-')) - 1
    
    res = 0
    
    while l >= 0:
        r = x%10
        x /= 10
        res += r * pow(10, l)
        l -= 1
    
    ans = int(res) * -1 if neg else int(res)
    
    if pow(-2, 31) <= ans <= pow(2, 31) - 1:
        return ans
    else:
        return 0



x = reverse2(-3210)
print(x)

