import pytest
from maximum_subarray import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_element_positive(solution):
    # Test case: Single positive element
    nums = [5]
    assert solution.maxSubArray(nums) == 5  # The only element is the largest sum


def test_single_element_negative(solution):
    # Test case: Single negative element
    nums = [-1]
    assert solution.maxSubArray(nums) == -1  # The only element is the largest sum


def test_all_positive_numbers(solution):
    # Test case: All positive numbers
    nums = [1, 2, 3, 4, 5]
    assert solution.maxSubArray(nums) == 15  # Sum of the entire array is the largest


def test_all_negative_numbers(solution):
    # Test case: All negative numbers
    nums = [-2, -3, -1, -5]
    assert (
        solution.maxSubArray(nums) == -1
    )  # The least negative number is the largest sum


def test_mixed_numbers(solution):
    # Test case: Mixed positive and negative numbers
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums) == 6  # The largest sum subarray is [4, -1, 2, 1]


def test_empty_array(solution):
    # Test case: Empty array (if allowed)
    nums = []
    with pytest.raises(IndexError):
        solution.maxSubArray(nums)  # Edge case: No elements in the array


def test_large_sum_in_middle(solution):
    # Test case: Large sum in the middle of the array
    nums = [1, 2, -1, -2, 10, -1, 2, -5, 1]
    assert (
        solution.maxSubArray(nums) == 12
    )  # Subarray [10, -1, 2, -5, 1] gives the max sum


def test_large_sum_at_beginning(solution):
    # Test case: Largest sum at the beginning
    nums = [5, 4, -1, 7, 8, -10, 1]
    assert (
        solution.maxSubArray(nums) == 23
    )  # Subarray [5, 4, -1, 7, 8] gives the max sum


def test_large_sum_at_end(solution):
    # Test case: Largest sum at the end
    nums = [-10, -1, 2, 3, 4, 5, 6]
    assert (
        solution.maxSubArray(nums) == 20
    )  # Subarray [2, 3, 4, 5, 6] gives the max sum


def test_alternating_large_and_small(solution):
    # Test case: Alternating large and small numbers
    nums = [100, -99, 100, -99, 100]
    assert (
        solution.maxSubArray(nums) == 201
    )  # Subarray [100, -99, 100, -99, 100] gives the max sum
