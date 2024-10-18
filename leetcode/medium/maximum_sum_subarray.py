# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        local_maximum = nums[0]
        maximum = nums[0]

        for i in range (1, len(nums)):
            local_maximum = max(nums[i] + local_maximum, nums[i])
            maximum = max(local_maximum, maximum)

        return maximum

solution = Solution()
print(solution.max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.max_subarray([1]))
print(solution.max_subarray([5,4,-1,7,8]))