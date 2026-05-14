"""
Problem: Subtract the Product and Sum of Digits of an Integer
LeetCode: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Given an integer number n, return the difference between the product of its digits
and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Extract digits using modulo and calculate product and sum.
        Time Complexity: O(log n) where n is the number (number of digits)
        Space Complexity: O(1)
        """
        product = 1
        sum_digits = 0
        
        # Extract each digit from right to left
        while n > 0:
            digit = n % 10  # Get the rightmost digit
            product *= digit
            sum_digits += digit
            n //= 10  # Remove the rightmost digit
        
        return product - sum_digits


# Alternative approach using string conversion
class SolutionString:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Convert to string and iterate through digits.
        Time Complexity: O(log n)
        Space Complexity: O(log n) for string storage
        """
        s = str(n)
        product = 1
        sum_digits = 0
        
        for digit_char in s:
            digit = int(digit_char)
            product *= digit
            sum_digits += digit
        
        return product - sum_digits


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n1 = 234
    print(f"Input: {n1}")
    result1 = solution.subtractProductAndSum(n1)
    print(f"Output: {result1}")
    print(f"Explanation: product = 2*3*4 = 24, sum = 2+3+4 = 9, difference = 24-9 = 15\n")
    
    # Test case 2
    n2 = 4421
    print(f"Input: {n2}")
    result2 = solution.subtractProductAndSum(n2)
    print(f"Output: {result2}")
    print(f"Explanation: product = 4*4*2*1 = 32, sum = 4+4+2+1 = 11, difference = 32-11 = 21")
