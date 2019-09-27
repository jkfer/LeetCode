"""
1201.
Ugly Number III

Difficulty:Medium
Write a program to find the n-th ugly number.
Ugly numbers are positive integers which are divisible by a or b or c.

Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]

"""

class Solution:
    # good solution - but for larger values it will timeout
    def nthUglyNumber(self, n, a, b, c):
        count = 0
        counter = 0
        # create an array of numbers until K = a*b*c
        R = []
        K = a*b*c
        # form the first array
        while count < K:
            if count % a == 0 or count % b == 0 or count % c == 0:
                R.append(count)
                counter += 1
            count += 1
        
        #print(counter)
        q = int(n/counter)
        r = int(n%counter)

        count = 0
        counter = 0
        """
        while count < K:
            if count % a == 0 or count % b == 0 or count % c == 0:
                counter += 1
            
            if counter == r+1:
                break
            else:
                count += 1
        """        
        # now count is the number you want the remander to be multiplied with
        #print(count, counter)
        #print(R[count])
        ans = q*K + R[r]
        print(ans)
        #print(q, r)
        #print(R, len(R))

S = Solution()
S.nthUglyNumber(5, 2, 11, 13)

