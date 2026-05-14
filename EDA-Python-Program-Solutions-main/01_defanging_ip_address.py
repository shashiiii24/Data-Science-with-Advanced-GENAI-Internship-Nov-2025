"""
Problem: Defanging an IP Address
LeetCode: https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP is obtained by replacing every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Simple and efficient solution using string replace.
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(n) for the new string
        """
        return address.replace(".", "[.]")


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    ip1 = "1.1.1.1"
    print(f"Input: {ip1}")
    print(f"Output: {solution.defangIPaddr(ip1)}")
    print(f"Expected: 1[.]1[.]1[.]1\n")
    
    # Test case 2
    ip2 = "255.100.50.0"
    print(f"Input: {ip2}")
    print(f"Output: {solution.defangIPaddr(ip2)}")
    print(f"Expected: 255[.]100[.]50[.]0")
