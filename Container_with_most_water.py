"""
Idea:
for each index of the array, find the number that is equal or less
and the furthest from it. Maintain a area variable.
"""


class Solution:
    # works - timing out for large inputs, bad complexity
    def maxArea(self, height):
        if len(height) == 2:
            return min(height)

        area = 0
        for i, num1 in enumerate(height):
            rem = height[i+1:]
            for j, num2 in enumerate(rem, start=i+1):
                a = (j-i) * min(num1, num2)
                if a > area:
                    area = a
        return area

    # two pointer solution = referred from discussions
    def maxArea2(self, height):
        if len(height) == 2:
            return min(height)

        # two pointers:
        area = maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            L, R = height[left], height[right]
            if L < R:
                area = (right - left) * L
                while height[left] <= L:
                    left += 1
            else:
                area = (right - left) * R
                while height[right] <= R and right > 0:
                    right -= 1

            if area > maxarea:
                maxarea = area

        return maxarea


S = Solution()
print(S.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
