# https://leetcode.com/problems/prison-cells-after-n-days/


class Solution:
    def get_next(self, cells):
        NN = [0, False, False, False, False, False, False, 0]
        for i in range(1, 7):
            if cells[i-1] == 0 and cells[i+1] == 0:
                NN[i] = 1
            elif cells[i-1] == 1 and cells[i+1] == 1:
                NN[i] = 1
            else:
                NN[i] = 0
        return NN

    def prisonAfterNDays(self, cells, N):
        reference = cells.copy()
        cycle, k, c = [], 0, 0

        if cells[0] == 1 or cells[7] == 1:
            cells = self.get_next(cells)
            c += 1

        while cells not in cycle:
            cycle.append(cells)
            cells = self.get_next(cells)
            k += 1

        N = (N - c) % k
        cells = reference.copy()
        for _ in range(c):
            cells = self.get_next(cells)

        for _ in range(N):
            cells = self.get_next(cells)

        return cells



S = Solution()
# print(S.get_next([0,1,0,1,1,0,0,1]))
L = [1, 1, 0, 0, 0, 0, 1, 1]
a = S.prisonAfterNDays(L, 7)
print(a)
