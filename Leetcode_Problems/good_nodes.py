# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def traverse(self, node, curr_max) -> None:
        if node == None:
            return

        if node.val >= curr_max:
            curr_max = node.val
            # print(node.val, curr_max)
            self.ans += 1

        self.traverse(node.left, curr_max)
        self.traverse(node.right, curr_max)

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, -1e9)

        return self.ans
