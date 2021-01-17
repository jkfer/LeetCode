# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        
        layers = int((n+1) / 2)
        s = 0
        e = n
        N = 1

        ANS = [[None for i in range(n)] for j in range(n)]

        for i in range(layers):
            for i in range(s, e):
                ANS[s][i] = N
                N += 1
            
            for i in range(s+1, e):
                ANS[i][e-1] = N
                N += 1
            
            for i in range(e-2, s-1, -1):
                ANS[e-1][i] = N
                N += 1
            
            for i in range(e-2, s, -1):
                ANS[i][s] = N
                N += 1
            
            s += 1
            e -= 1
        
        return ANS



S = Solution()
print(S.generateMatrix(4))



