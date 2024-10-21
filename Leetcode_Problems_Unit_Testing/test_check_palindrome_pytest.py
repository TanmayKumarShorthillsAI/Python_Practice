import pytest
from check_palindrome import Solution1


@pytest.fixture
def solution():
    return Solution1()


def test_palindrome_positive(solution):
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(1221) == True
    assert solution.isPalindrome(0) == True
    assert solution.isPalindrome(1) == True


def test_non_palindrome(solution):
    assert solution.isPalindrome(123) == False
    assert solution.isPalindrome(10) == False


def test_negative_numbers(solution):
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(-1221) == False


def test_non_integer_arguments(solution):
    with pytest.raises(TypeError):
        solution.isPalindrome("121")
    with pytest.raises(TypeError):
        solution.isPalindrome(12.21)
    with pytest.raises(TypeError):
        solution.isPalindrome(None)
    with pytest.raises(TypeError):
        solution.isPalindrome([121])
