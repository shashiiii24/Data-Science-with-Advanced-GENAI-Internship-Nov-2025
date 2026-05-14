"""
Problem: Find Numbers with an Even Number of Digits
LeetCode: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Count numbers with even number of digits.
        Time Complexity: O(n * m) where n is array length, m is avg digit count
        Space Complexity: O(1)
        """
        count = 0
        for num in nums:
            # Count digits by converting to string
            if len(str(num)) % 2 == 0:
                count += 1
        return count


# Alternative approach using bit manipulation for more efficiency
class SolutionOptimized:
    def findNumbers(self, nums: list[int]) -> int:
        """
        More optimized approach using mathematical method.
        """
        count = 0
        for num in nums:
            digits = 0
            while num > 0:
                digits += 1
                num //= 10
            if digits % 2 == 0:
                count += 1
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [12, 345, 2, 6, 7896]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findNumbers(nums1)}")
    print(f"Expected: 2\n")
    
    # Test case 2
    nums2 = [555, 901, 482, 1771]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findNumbers(nums2)}")
    print(f"Expected: 1")
