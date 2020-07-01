# https://leetcode.com/problems/unique-paths/
# Medium


class Solution:
    def uniquePaths(self, m, n):
        if n == 1 and m == 1:
            return 1
        possib = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    possib[i][j] = 0
                elif i == 0 and j > 0:
                    possib[i][j] = 1
                elif j == 0 and i > 0:
                    possib[i][j] = 1
                else:
                    possib[i][j] = possib[i-1][j] + possib[i][j-1]
        return possib[n-1][m-1]


S = Solution()
ans = S.uniquePaths(5, 99)
print(ans)
