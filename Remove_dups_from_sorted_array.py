# remove the dups without allocating another array in the memory
# return the length of the value and also the fixed array that does not have any duplicates

nums = [0, 4, 4]

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) in [0, 1]:
            return len(nums)

        j = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[-1]
        nums = nums[:j+1]

        return j+1


L = Solution()
x = L.removeDuplicates(nums)
print(x)
