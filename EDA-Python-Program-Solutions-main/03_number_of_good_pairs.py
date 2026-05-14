"""
Problem: Number of Good Pairs
LeetCode: https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums, return the number of good pairs.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Brute force approach using nested loops.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


# Optimized approach using Hash Map
class SolutionOptimized:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Using hash map to count occurrences.
        For n occurrences of a value, good pairs = n * (n - 1) / 2
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count_map = {}
        good_pairs = 0
        
        for num in nums:
            if num in count_map:
                # Add the count of this number we've seen so far
                good_pairs += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        return good_pairs


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1, 1, 3]
    print(f"Input: {nums1}")
    print(f"Output: {solution.numIdenticalPairs(nums1)}")
    print(f"Expected: 4\n")
    
    # Test case 2
    nums2 = [1, 1, 1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.numIdenticalPairs(nums2)}")
    print(f"Expected: 6")
