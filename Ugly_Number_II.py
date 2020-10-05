# https://leetcode.com/problems/ugly-number-ii/

import math
import collections


class Solution:
    def is_prime(self, n):
        j = (n // 2) + 1
        for k in range(2, j + 1):
            if n % k == 0:
                return False
        return True

    def good_divisors(self, n, primes):
        if self.is_prime(n):
            primes[n] = True
            return False

        c = (n // 2) + 1

        for i in range(2, c + 1):
            if n % i == 0 and self.is_prime(i):
                if i not in [2, 3, 5]:
                    return False
        return True

    # very slow - good for upto 100
    def nthUglyNumber(self, n):
        ans = [1, 2, 3, 4, 5]
        if n <= 5:
            return ans[n-1]

        i = 6
        primes = collections.defaultdict(bool)
        valid = collections.defaultdict(bool)
        for i in ans:
            valid[i] = True

        while len(ans) <= n:
            if i % 2 == 0:
                j = int(i / 2)
                if valid[j]:
                    ans.append(i)
                    valid[i] = True
            elif self.good_divisors(i, primes):
                ans.append(i)
                valid[i] = True
            i += 1

        return ans[n-1]

    # Referred solution:
    def nthUglyNumber2(self, n):
        res = [1]
        i2 = i3 = i5 = 0
        while len(res) < n:
            nxt = min([res[i2]*2, res[i3]*3, res[i5]*5])
            res.append(nxt)
            if nxt == res[i2]*2:
                i2 += 1
            if nxt == res[i3]*3:
                i3 += 1
            if nxt == res[i5]*5:
                i5 += 1
        return res[-1]


S = Solution()
for i in range(1, 1690):
    x = S.nthUglyNumber2(i)
    print(i, "-->", x)
