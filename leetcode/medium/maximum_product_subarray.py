# Given an integer array nums, find a subarray that has the largest product, and return the product.
#
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

from typing import List


class Solution:
    def max_product(self, nums: List[int]) -> int:
        max_product = min_product = result = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]

            if current < 0:
                max_product, min_product = min_product, max_product

            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)

            result = max(result, max_product)

        return result
