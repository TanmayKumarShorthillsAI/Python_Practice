# Check if the number provide is a palindrome
# Leetcode problem number: 9, URL: https://leetcode.com/problems/palindrome-number/description/
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if not isinstance(x, (int,)):
            raise TypeError("Type in not int")
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
