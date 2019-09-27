# remove the given element from the array
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

nums = [1]
val = 1

class Solution:
    def removeElement(self, nums, val):
        if len(nums) in [0]:
            print(nums, len(nums))

        j = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                nums[j] = nums[i]
                j += 1
        nums = nums[:len(nums) - count]
        print(nums, len(nums))

L = Solution()
L.removeElement(nums, val)