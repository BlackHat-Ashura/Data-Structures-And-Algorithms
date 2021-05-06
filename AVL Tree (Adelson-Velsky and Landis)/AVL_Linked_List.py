class AVLNode:
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None
        self.height = 1

    '''
    ===================================================================================================
    [+] Traversal, Searching and Tree Deletion in AVL Tree is same as that of Binary Search Tree (BST).
    ===================================================================================================
    '''

    def preOrderTraversal(self):
        def compute(node):
            if node is None:
                return ""
            else:
                result = [str(node.data)]
                if node.leftNode:
                    result += compute(node.leftNode)
                if node.rightNode:
                    result += compute(node.rightNode)
                return result

        values = compute(self)
        print("[+] Pre Order Traversal = " + " ".join(values) + "\n")

    def inOrderTraversal(self):
        def compute(node):
            result = []
            if node is None:
                return ""
            else:
                if node.leftNode:
                    result += compute(node.leftNode)
                result += [str(node.data)]
                if node.rightNode:
                    result += compute(node.rightNode)
                return result

        values = compute(self)
        print("[+] In Order Traversal = " + " ".join(values) + "\n")

    def postOrderTraversal(self):
        def compute(node):
            result = []
            if node is None:
                return ""
            else:
                if node.leftNode:
                    result += compute(node.leftNode)
                if node.rightNode:
                    result += compute(node.rightNode)
                result += [str(node.data)]
                return result

        values = compute(self)
        print("[+] Post Order Traversal = " + " ".join(values) + "\n")

    def levelOrderTraversal(self):
        queue = [self]
        print("[+] Level Order Traversal = ", end="")
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.leftNode:
                queue.insert(0, node.leftNode)
            if node.rightNode:
                queue.insert(0, node.rightNode)
        print("\n")

    def search(self, value):
        def compute(node, value):
            if node.data == value:
                return True
            elif value < node.data:
                if node.leftNode:
                    return compute(node.leftNode, value)
            elif value > node.data:
                if node.rightNode:
                    return compute(node.rightNode, value)

        if compute(self, value):
            print(f"[+] {value} exists.\n")
        else:
            print(f"[-] {value} doesn't exist.\n")

    def deleteAVL(self):
        self.data = None
        self.leftNode = None
        self.rightNode = None

    '''=============================================================================================='''


'''============================== Helper Functions =============================='''


def getHeight(node):
    if node is None:
        return 0
    return node.height


def rightRotate(node):
    newRoot = node.leftNode
    node.leftNode = newRoot.rightNode
    newRoot.rightNode = node
    node.height = 1 + max(getHeight(node.leftNode), getHeight(node.rightNode))
    newRoot.height = 1 + max(getHeight(newRoot.leftNode), getHeight(newRoot.rightNode))
    return newRoot


def leftRotate(node):
    newRoot = node.rightNode
    node.rightNode = newRoot.leftNode
    newRoot.leftNode = node
    node.height = 1 + max(getHeight(node.leftNode), getHeight(node.rightNode))
    newRoot.height = 1 + max(getHeight(newRoot.leftNode), getHeight(newRoot.rightNode))
    return newRoot


def checkBalance(node):
    if node is None:
        return 0
    return getHeight(node.leftNode) - getHeight(node.rightNode)


'''====================================================================================================='''

'''============================== Insertion =============================='''


def insertNode(node, value):
    if node is None:
        return AVLNode(value)
    if node.data is None:
        node.data = value
    elif value < node.data:
        node.leftNode = insertNode(node.leftNode, value)
    else:
        node.rightNode = insertNode(node.rightNode, value)

    node.height = 1 + max(getHeight(node.leftNode), getHeight(node.rightNode))
    balance = checkBalance(node)

    ''' For Left-Left condition. '''
    if balance > 1 and value < node.leftNode.data:
        return rightRotate(node)

    ''' For Left-Right condition. '''
    if balance > 1 and value > node.leftNode.data:
        node.leftNode = leftRotate(node.leftNode)
        return rightRotate(node)

    ''' For Right-Right condition. '''
    if balance < -1 and value > node.rightNode.data:
        return leftRotate(node)

    ''' For Right-Left condition. '''
    if balance < -1 and value < node.rightNode.data:
        node.rightNode = rightRotate(node.rightNode)
        return leftRotate(node)
    return node


'''====================================================================================================='''

'''============================== Deletion =============================='''


def minNode(node):
    if node is None:
        return None
    return minNode(node.leftNode)


def delNode(node, value):
    if node is None:
        return None
    elif value < node.data:
        node.leftNode = delNode(node.leftNode, value)
    elif value > node.data:
        node.rightNode = delNode(node.rightNode, value)
    else:
        if node.leftNode is None:
            return node.rightNode

        if node.rightNode is None:
            return node.leftNode

        temp = minNode(node.rightNode)
        node.data = temp.data
        node.rightNode = delNode(node.rightNode, temp.data)

    balance = checkBalance(node)
    ''' For Left-Left condition. '''
    if balance > 1 and checkBalance(node.leftNode) >= 0:
        return rightRotate(node)

    ''' For Left-Right condition. '''
    if balance > 1 and checkBalance(node.leftNode) < 0:
        node.leftNode = leftRotate(node.leftNode)
        return rightRotate(node)

    ''' For Right-Right condition. '''
    if balance < -1 and checkBalance(node.rightNode) <= 0:
        return leftRotate(node)

    ''' For Right-Left condition. '''
    if balance < -1 and checkBalance(node.rightNode) > 0:
        node.rightNode = rightRotate(node.rightNode)
        return leftRotate(node)
    return node


'''====================================================================================================='''

# tree = AVLNode()
# tree = insertNode(tree, 5)
# tree.levelOrderTraversal()
# tree = insertNode(tree, 10)
# tree.levelOrderTraversal()
# tree = insertNode(tree, 15)
# tree.levelOrderTraversal()
# tree = insertNode(tree, 20)
# tree.levelOrderTraversal()
# tree = delNode(tree, 20)
# tree.levelOrderTraversal()
# tree = insertNode(tree, 11)
# tree.levelOrderTraversal()
# tree = insertNode(tree, 12)
# tree.levelOrderTraversal()
