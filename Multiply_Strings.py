# 43
# 43. Multiply Strings

num1 = "45696"
num2 = "1235"



class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return 0

        ANS = []

        for n in num2[::-1]:
            small_ans = []
            carry = 0
            for k in num1[::-1]:
                n = ord(str(n)) - 48
                k = ord(str(k)) - 48
                a = n * k
                
                if carry > 0:
                    a += carry
                
                a = str(a)
                if len(a) > 1:
                    carry = int(a[0])
                    a = a[1]
                else:
                    carry = 0

                small_ans.append(a)

            if carry == 0:
                ANS.append(("".join(small_ans[::-1])))
            else:
                ANS.append(str(carry) + ("".join(small_ans[::-1])))
        
        #print(ANS)
        j = len(ANS) - 1
        for i, num in enumerate(ANS):
            ANS[i] = "0" * j + num + "0" * i
            j -= 1
        
        #print(ANS)

        ANS = zip(*ANS)

        carry = 0
        SUM = []
        for L in ANS[::-1]:
            small_sum = 0
            for n in L:
                small_sum += ord(n) - 48
            
            if carry > 0:
                small_sum += carry
            
            small_sum = str(small_sum)
            
            if len(small_sum) > 1:
                carry = int(small_sum[0])
                small_sum = small_sum[1]
            else:
                carry = 0
            
            SUM.append(small_sum)
        
        if carry == 0:
            return "".join(SUM[::-1])
        else:
            return str(carry) + "".join(SUM[::-1])
            


S = Solution()
print(S.multiply(num1, num2))


from math import pow

def multip(num1, num2):
    n1 = n2 = 0
    for i, num in enumerate(num1):
        n1 += (ord(num) - 48) * int(pow(10, len(num1) - 1 - i))
    
    for i, num in enumerate(num2):
        n2 += (ord(num) - 48) * int(pow(10, len(num2) - 1 - i))
    
    return str(n1*n2)

print(multip(num1, num2))
