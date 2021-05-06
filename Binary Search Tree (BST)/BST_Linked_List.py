class BST:
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    def insertNode(self, value):
        if self.data is None:
            self.data = value
            print(f"[+] Successfully added {value} as First Node.\n")
        else:
            newNode = BST(value)
            if value <= self.data:
                if self.leftNode:
                    self.leftNode.insertNode(value)
                else:
                    self.leftNode = newNode
                    print(f"[+] Successfully added {value} to {self.data}.\n")
            else:
                if self.rightNode:
                    self.rightNode.insertNode(value)
                else:
                    self.rightNode = newNode
                    print(f"[+] Successfully added {value} to {self.data}.\n")

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

    def minNode(self):
        current = self
        while current.leftNode:
            current = current.leftNode
        return current

    def deleteNode(self, value):
        if self.data is None:
            '''Comes here when BST is empty.'''
            return self
        if value < self.data:
            self.leftNode = self.leftNode.deleteNode(value)
        elif value > self.data:
            self.rightNode = self.rightNode.deleteNode(value)
        else:
            if self.leftNode is None:
                '''Comes here when Node to be deleted has 1 or 0 Child.'''
                temp = self.rightNode
                self.rightNode = None
                return temp
            if self.rightNode is None:
                '''Comes here when Node to be deleted has 1 Child, that is the Left Child.'''
                temp = self.leftNode
                self.leftNode = None
                return temp
            '''
            Comes here when Node to be deleted has 2 Children.
            The Node to be deleted is replaced with SMALLEST GREATER value.
            temp = self.rightNode.minNode()
            self.rightNode --> GREATER value than Current Node
            .minNode() --> Returns SMALLEST value after Current Node
            '''
            temp = self.rightNode.minNode()
            self.data = temp.data
            self.rightNode = self.rightNode.deleteNode(temp.data)
        return self

    def deleteBST(self):
        self.data = None
        self.leftNode = None
        self.rightNode = None


# tree = BST()
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
# tree.search(70)
# tree.search(101)
# tree.levelOrderTraversal()
# tree.deleteNode(70)
# tree.levelOrderTraversal()
# tree.deleteBST()
# tree.levelOrderTraversal()
