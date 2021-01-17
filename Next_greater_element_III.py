# https://leetcode.com/problems/next-greater-element-iii/

# referred solution:
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        N = list(str(n))
        i = len(N) - 1

        while i > 0 and int(N[i-1]) >= int(N[i]):
            i -= 1
        
        if i == 0:
            return -1
        
        j = i
        
        while j+1 < len(N) and N[j+1] > N[i-1]:
            j += 1
        
        N[i-1], N[j] = N[j], N[i-1]
        N[i:] = N[i:][::-1]
        ret = int(''.join(N))

        return ret if ret < 1<<31 else -1

N = 234157641
# print(N)
S = Solution()
print(S.nextGreaterElement(N))
