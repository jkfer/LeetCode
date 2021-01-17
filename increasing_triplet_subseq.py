# https://leetcode.com/problems/increasing-triplet-subsequence/

# referred solution:
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = second_smallest = float('inf')

        for num in nums:
            if num < smallest:
                smallest = num
            if smallest < num < second_smallest:
                second_smallest = num
            if num > second_smallest:
                return True

        return False
