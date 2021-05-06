"""
Implement a function to check if a Binary Tree is a BST.
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def mini(root):
    if root.left is None and root.right is None:
        return root.val
    Leftmin = mini(root.left)
    Rightmin = mini(root.right)
    return min(Leftmin, Rightmin)


def maxi(root):
    if root.left is None and root.right is None:
        return root.val
    Leftmax = maxi(root.left)
    Rightmax = maxi(root.right)
    return max(Leftmax, Rightmax)


def isValidBST(root):
    if root.left is None and root.right is None:
        return True
    if maxi(root.left) > root.val or mini(root.right) < root.val:
        return False
    if isValidBST(root.left) and isValidBST(root.right):
        return True
    else:
        return False
