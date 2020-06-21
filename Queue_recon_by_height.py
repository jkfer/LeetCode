# https://leetcode.com/problems/queue-reconstruction-by-height/
# 406


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda item: (-item[0], item[1]))
        ANS = []
        in_arr = 0

        for i, n in enumerate(people):
            if not ANS:
                ANS.append(n)
                in_arr += 1
            else:
                h, f = n
                k = in_arr
                while k > f and ANS[k-1][0] >= h:
                    k -= 1
                ANS.insert(k, n)
                in_arr += 1

        return ANS


L = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7],
     [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
S = Solution()
print(S.reconstructQueue(L))
