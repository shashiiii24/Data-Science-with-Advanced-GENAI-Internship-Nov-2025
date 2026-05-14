"""
Problem: How Many Numbers Are Smaller Than the Current Number
LeetCode: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Given the array nums, for each nums[i] find how many numbers in the array are
smaller than it. That is, for each nums[i] you have to count the number of valid j's
such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Brute force approach using nested loops.
        Time Complexity: O(n^2)
        Space Complexity: O(1) (not counting output array)
        """
        result = []
        for i in range(len(nums)):
            smaller_count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    smaller_count += 1
            result.append(smaller_count)
        return result


# Optimized approach using sorting
class SolutionOptimized:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Optimized using sorted array to find rank.
        Time Complexity: O(n log n) for sorting + O(n) for lookup = O(n log n)
        Space Complexity: O(n) for sorted array
        """
        # Create array of (value, original_index) and sort
        indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
        result = [0] * len(nums)
        
        for rank, (original_idx, value) in enumerate(indexed_nums):
            result[original_idx] = rank
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [8, 1, 2, 2, 3]
    print(f"Input: {nums1}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums1)}")
    print(f"Expected: [4, 0, 1, 1, 2]\n")
    
    # Test case 2
    nums2 = [1, 2, 3]
    print(f"Input: {nums2}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums2)}")
    print(f"Expected: [0, 1, 2]")
