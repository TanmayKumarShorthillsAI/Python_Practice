import unittest
import check_palindrome


class TestCodes(unittest.TestCase):

    def setUp(self):
        self.check = check_palindrome.Solution1()

    def test_palindrome_positive(self):
        self.assertTrue(self.check.isPalindrome(121))
        self.assertTrue(self.check.isPalindrome(1221))
        self.assertTrue(self.check.isPalindrome(0))

    def test_palindrome_negative(self):
        self.assertFalse(self.check.isPalindrome(-121))
        self.assertFalse(self.check.isPalindrome(-1221))

    def test_non_palindrome(self):
        self.assertFalse(self.check.isPalindrome(123))
        self.assertFalse(self.check.isPalindrome(1234))

    def test_edge_cases(self):
        self.assertTrue(self.check.isPalindrome(1))  # Single digit is a palindrome
        self.assertTrue(
            self.check.isPalindrome(11)
        )  # Two identical digits are a palindrome
        self.assertFalse(self.check.isPalindrome(10))  # 10 is not a palindrome

    def test_non_integer_arguments(self):
        with self.assertRaises(TypeError):
            self.check.isPalindrome("121")  # String input
        with self.assertRaises(TypeError):
            self.check.isPalindrome(12.21)  # Float input
        with self.assertRaises(TypeError):
            self.check.isPalindrome(None)  # None input
        with self.assertRaises(TypeError):
            self.check.isPalindrome([])  # List input
        with self.assertRaises(TypeError):
            self.check.isPalindrome({})  # Dictionary input


if __name__ == "__main__":
    unittest.main()
