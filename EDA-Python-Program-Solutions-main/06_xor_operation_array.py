"""
Problem: XOR Operation in an Array
LeetCode: https://leetcode.com/problems/xor-operation-in-an-array/

Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Calculate XOR of array elements using formula.
        Array: [start, start+2, start+4, ..., start+2*(n-1)]
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        
        for i in range(n):
            # Calculate element: start + 2*i
            num = start + 2 * i
            # XOR with result
            result ^= num
        
        return result


# Alternative: Generate array then XOR
class SolutionArray:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Generate array and use reduce with XOR.
        Time Complexity: O(n)
        Space Complexity: O(n) for array
        """
        nums = [start + 2*i for i in range(n)]
        result = 0
        for num in nums:
            result ^= num
        return result


# Using functools.reduce
from functools import reduce
import operator

class SolutionReduce:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Using reduce with XOR operator.
        """
        nums = [start + 2*i for i in range(n)]
        return reduce(operator.xor, nums, 0)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n1, start1 = 5, 0
    print(f"Input: n = {n1}, start = {start1}")
    result1 = solution.xorOperation(n1, start1)
    print(f"Output: {result1}")
    print(f"Array: [0, 2, 4, 6, 8], XOR: 0^2^4^6^8 = 12\n")
    
    # Test case 2
    n2, start2 = 4, 3
    print(f"Input: n = {n2}, start = {start2}")
    result2 = solution.xorOperation(n2, start2)
    print(f"Output: {result2}")
    print(f"Array: [3, 5, 7, 9], XOR: 3^5^7^9 = 12")
