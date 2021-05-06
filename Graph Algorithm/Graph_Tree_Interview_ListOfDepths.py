"""
Given a binary search tree,
design an algorithm which creates a linked list of all the nodes at each depth
(that is, if you have a tree with depth D, you’ll have D linked lists)
"""


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        LeftDepth = 1 + depth(tree.left)
        RightDepth = 1 + depth(tree.right)
    if LeftDepth > RightDepth:
        return LeftDepth
    else:
        return RightDepth


def treeToLinkedList(tree, custDict={}, d=None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) is None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
    if tree.left != None:
        treeToLinkedList(tree.left, custDict, d - 1)
    if tree.right != None:
        treeToLinkedList(tree.right, custDict, d - 1)
    return custDict
