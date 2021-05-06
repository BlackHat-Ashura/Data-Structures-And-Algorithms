"""
Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree
such that the heights of the two subtrees of any node never differ by more than one.
"""


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1

    return max(leftHeight, rightHeight) + 1


def isBalanced(root):
    return isBalancedHelper(root) > -1
