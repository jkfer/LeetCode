# https://leetcode.com/problems/next-greater-element-ii/

# Referred solution
class Solution:
    def nextGreaterElements(self, nums):
        if len(nums) == 1:
            return [-1]
        
        res = [None] * len(nums)
        S = []

        for _ in range(2):
            for i in range(len(nums)-1, -1, -1):
                if not S:
                    S.append(i)
                    res[i] = -1
                else:
                    if nums[S[-1]] > nums[i]:
                        res[i] = nums[S[-1]]
                        S.append(i)
                    else:
                        while S and nums[S[-1]] <= nums[i]:
                            S.pop()
                        if not S:
                            S.append(i)
                            res[i] = -1
                        else:
                            res[i] = nums[S[-1]]
                            S.append(i)
        
        return res

nums = [3, 8, 4, 1, 2]
S = Solution()
ans = S.nextGreaterElements(nums)
print(ans)
            
