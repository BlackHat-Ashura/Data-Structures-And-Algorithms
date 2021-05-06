class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    def insertNode(self, value):
        if self.data is None:
            self.data = value
            print(f"[+] Successfully added {value} as First Node.\n")
        else:
            newNode = BinaryTree(value)
            queue = [self]
            while queue:
                node = queue.pop()
                if node.leftNode:
                    queue.insert(0, node.leftNode)
                else:
                    node.leftNode = newNode
                    print(f"[+] Successfully added {newNode.data} to {node.data}.\n")
                    break
                if node.rightNode:
                    queue.insert(0, node.rightNode)
                else:
                    node.rightNode = newNode
                    print(f"[+] Successfully added {newNode.data} to {node.data}.\n")
                    break

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
        queue = [self]
        while queue:
            node = queue.pop()
            if node.data == value:
                print(f"[+] {value} exists.\n")
                return
            if node.leftNode:
                queue.insert(0, node.leftNode)
            if node.rightNode:
                queue.insert(0, node.rightNode)
        print(f"[-] {value} doesn't exist.\n")

    def getDeepestNode(self):
        queue = [self]
        deepestNode = None
        while queue:
            deepestNode = queue.pop()
            if deepestNode.leftNode:
                queue.insert(0, deepestNode.leftNode)
            if deepestNode.rightNode:
                queue.insert(0, deepestNode.rightNode)
        return deepestNode

    def delDeepestNode(self):
        deepestNode = self.getDeepestNode()
        queue = [self]
        if self == deepestNode:
            '''Only in case of Single Node'''
            self.data = None
            return
        while queue:
            node = queue.pop()
            if node.leftNode:
                if node.leftNode == deepestNode:
                    node.leftNode = None
                    return
                else:
                    queue.insert(0, node.leftNode)
            if node.rightNode:
                if node.rightNode == deepestNode:
                    node.rightNode = None
                    return
                else:
                    queue.insert(0, node.rightNode)

    def delNode(self, value):
        queue = [self]
        while queue:
            node = queue.pop()
            if node.data == value:
                node.data = self.getDeepestNode().data
                self.delDeepestNode()
                print(f"[+] {value} deleted.\n")
                return
            if node.leftNode:
                queue.insert(0, node.leftNode)
            if node.rightNode:
                queue.insert(0, node.rightNode)
        print(f"[-] {value} not found.\n")

    def delBT(self):
        self.data = None
        self.leftNode = None
        self.rightNode = None


# tree = BinaryTree()
# tree.insertNode(70)
# tree.insertNode(50)
# tree.insertNode(90)
# tree.insertNode(30)
# tree.insertNode(60)
# tree.insertNode(80)
# tree.insertNode(100)
# tree.insertNode(20)
# tree.insertNode(40)
# tree.insertNode(85)
# tree.levelOrderTraversal()
# tree.preOrderTraversal()
# tree.inOrderTraversal()
# tree.postOrderTraversal()

# tree.search(20)
# tree.search(200)
# print(tree.getDeepestNode().data)

# tree.levelOrderTraversal()
# tree.delDeepestNode()
# tree.levelOrderTraversal()

# tree.levelOrderTraversal()
# tree.delNode(100)
# tree.levelOrderTraversal()
