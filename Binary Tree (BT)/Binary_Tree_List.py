class BinaryTree:
    def __init__(self, size):
        self.list = [None] * size
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            print("[!] Binary Tree is full.\n")
        else:
            self.list[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            print(f"[+] Successfully added {value} to {self.list[self.lastUsedIndex//2]}.\n")

    def searchNode(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                print(f"[+] {value} exists in Binary Tree.\n")
                return
        print(f"[-] {value} doesn't exist in Binary Tree.\n")

    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.list[index])
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal(2 * index + 1)

    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2 * index)
        print(self.list[index])
        self.inOrderTraversal(2 * index + 1)

    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2 * index)
        self.postOrderTraversal(2 * index + 1)
        print(self.list[index])

    def levelOrderTraversal(self):
        for i in range(1, self.lastUsedIndex+1):
            print(self.list[i])

    def delNode(self, value):
        if self.lastUsedIndex == 0:
            print("[-] No node to delete.\n")
        else:
            for i in range(1, self.lastUsedIndex+1):
                if self.list[i] == value:
                    self.list[i] = self.list[self.lastUsedIndex]
                    self.list[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    print(f"[+] {value} deleted.\n")
                    return
            print(f"[-] {value} not found.\n")

    def delete(self):
        self.list = [None] * self.maxSize
        self.lastUsedIndex = 0


# tree = BinaryTree(8)
# tree.insertNode("Drinks")
# tree.insertNode("Hot")
# tree.insertNode("Cold")
# tree.insertNode("Tea")
# tree.insertNode("Coffee")
# tree.insertNode("Cola")

# tree.searchNode("Hot")
# tree.searchNode("Heat")

# tree.preOrderTraversal()
# print()
# tree.inOrderTraversal()
# print()
# tree.postOrderTraversal()
# print()
# tree.levelOrderTraversal()
# print()
# tree.delNode("Hot")
# tree.levelOrderTraversal()
