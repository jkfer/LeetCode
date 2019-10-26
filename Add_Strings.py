# 415

from math import pow

def multip(num1, num2):
    n1 = n2 = 0
    for i, num in enumerate(num1):
        n1 += (ord(num) - 48) * int(pow(10, len(num1) - 1 - i))
    
    for i, num in enumerate(num2):
        n2 += (ord(num) - 48) * int(pow(10, len(num2) - 1 - i))
    
    return str(n1+n2)


num1 = "123"
num2 = "456"
print(multip(num1, num2))