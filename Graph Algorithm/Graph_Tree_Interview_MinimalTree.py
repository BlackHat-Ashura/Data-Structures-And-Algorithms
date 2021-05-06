"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimalTree(sortedArray):
    n = len(sortedArray)
    mid = n//2
    if n == 0:
        return None
    if n == 1:
        return sortedArray[0]
    mid_element = sortedArray[mid]
    Left_ar = minimalTree(sortedArray[:mid])
    Right_ar = minimalTree(sortedArray[mid+1:])

    node = BSTNode(mid_element, Left_ar, Right_ar)
    return node
