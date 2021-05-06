"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def Search(value, node):
    if node is None:
        return False
    if node == value:
        return True
    return Search(value, node.left) or Search(value, node.right)


def findFirstCommonAncestor(n1, n2, root):
    if root.left is None and root.right is None:
        return False
    if Search(n1, root.right) and Search(n2, root.right):
        return findFirstCommonAncestor(n1, n2, root.right)
    if Search(n1, root.left) and Search(n2, root.left):
        return findFirstCommonAncestor(n1, n2, root.left)
    if (Search(n1, root.right) and Search(n2, root.left)) or (Search(n1, root.left) and Search(n2, root.right)):
        return root.value
