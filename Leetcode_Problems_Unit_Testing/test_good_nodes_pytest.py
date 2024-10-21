import pytest
from good_nodes import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@pytest.fixture
def solution():
    return Solution()


def test_single_node_tree(solution):
    # Tree with a single node
    root = TreeNode(1)
    assert (
        solution.goodNodes(root) == 1
    )  # There's only one node, which is a "good node"


def test_complete_binary_tree(solution):
    # Tree structure:
    #       3
    #      / \
    #     1   4
    #    /   / \
    #   3   1   5
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    assert solution.goodNodes(root) == 4  # Expected good nodes are: 3, 3, 4, 5


def test_left_skewed_tree(solution):
    # Tree structure (left-skewed):
    #    2
    #   /
    #  1
    root = TreeNode(2)
    root.left = TreeNode(1)

    assert solution.goodNodes(root) == 1  # Only the root (2) is a "good node"


def test_right_skewed_tree(solution):
    # Tree structure (right-skewed):
    #    1
    #     \
    #      2
    #       \
    #        3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    assert (
        solution.goodNodes(root) == 3
    )  # All nodes are good since each node is greater than the previous


def test_all_same_value_tree(solution):
    # Tree structure where all nodes have the same value:
    #    1
    #   / \
    #  1   1
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)

    assert (
        solution.goodNodes(root) == 3
    )  # All nodes are good since they all have the same value


def test_none_root_tree(solution):
    # Edge case: The tree is None (empty tree)
    root = None
    assert solution.goodNodes(root) == 0  # No nodes, so no "good nodes"


def test_tree_with_negative_values(solution):
    # Tree structure with negative values:
    #       -10
    #       /  \
    #     -20   -5
    #     /      \
    #   -30      -1
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.left.left = TreeNode(-30)
    root.right = TreeNode(-5)
    root.right.right = TreeNode(-1)

    assert solution.goodNodes(root) == 3  # Expected good nodes are: -10, -5, -1


def test_tree_with_duplicate_good_nodes(solution):
    # Tree structure:
    #       10
    #       / \
    #     10   10
    #    /       \
    #   10       10
    root = TreeNode(10)
    root.left = TreeNode(10)
    root.left.left = TreeNode(10)
    root.right = TreeNode(10)
    root.right.right = TreeNode(10)

    assert (
        solution.goodNodes(root) == 5
    )  # All nodes are good since they are equal to their ancestors


def test_unbalanced_tree(solution):
    # Unbalanced tree structure:
    #       7
    #      /
    #     3
    #      \
    #       6
    #         \
    #          5
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.left.right = TreeNode(6)
    root.left.right.right = TreeNode(5)

    assert solution.goodNodes(root) == 1  # Expected good nodes are: 7


def test_large_values_tree(solution):
    # Tree with very large values:
    #          1000000
    #         /       \
    #   -1000000    1000000000
    root = TreeNode(1000000)
    root.left = TreeNode(-1000000)
    root.right = TreeNode(1000000000)

    assert solution.goodNodes(root) == 2  # Expected good nodes are: 1000000, 1000000000


def test_single_path_tree(solution):
    # Tree structure (linear tree, one path):
    #    4
    #     \
    #      3
    #       \
    #        2
    #         \
    #          1
    root = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    assert solution.goodNodes(root) == 1  # Only the root (4) is a "good node"
