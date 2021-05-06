class Heap:
    def __init__(self, size, heapType="Min"):
        self.list = [None] * (size + 1)
        self.heapSize = 0
        self.maxSize = size + 1
        self.heapType = heapType

    def peek(self):
        return self.list[1]

    def size(self):
        return self.heapSize

    def levelOrderTraversal(self):
        for i in range(1, self.heapSize + 1):
            print(self.list[i], end=" ")
        print("\n")

    def heapifyTreeInsert(self, index):
        parentIndex = int(index/2)
        if index <= 1:
            return
        if self.heapType == 'Min':
            if self.list[index] < self.list[parentIndex]:
                temp = self.list[index]
                self.list[index] = self.list[parentIndex]
                self.list[parentIndex] = temp
        elif self.heapType == 'Max':
            if self.list[index] > self.list[parentIndex]:
                temp = self.list[index]
                self.list[index] = self.list[parentIndex]
                self.list[parentIndex] = temp
        self.heapifyTreeInsert(parentIndex)

    def insertNode(self, value):
        if self.heapSize + 1 == self.maxSize:
            print("[!] Heap is full.")
        else:
            self.list[self.heapSize + 1] = value
            self.heapSize += 1
            self.heapifyTreeInsert(self.heapSize)

    def heapifyTreeExtract(self, index):
        left = index * 2
        right = index * 2 + 1
        swap = 0
        if self.heapSize < left:
            '''
            Comes here when Root Node is moving to the right of Tree.
            Since elements are inserted first to the left,
            if "heapSize < left" then current Right Node has no Children.
            '''
            return
        elif self.heapSize == left:
            '''
            Comes here only when Root Node is moving to the right of Tree
            and has only one Child, that is the Left Child.
            '''
            if self.heapType == "Min":
                if self.list[index] > self.list[left]:
                    temp = self.list[index]
                    self.list[index] = self.list[left]
                    self.list[left] = temp
                    return
            elif self.heapType == 'Max':
                if self.list[index] < self.list[left]:
                    temp = self.list[index]
                    self.list[index] = self.list[left]
                    self.list[left] = temp
                    return
        else:
            '''
            Comes here when Moving Node has 2 Children.
            '''
            if self.heapType == "Min":
                if self.list[left] < self.list[right]:
                    swap = left
                else:
                    swap = right
                if self.list[index] > self.list[swap]:
                    temp = self.list[index]
                    self.list[index] = self.list[left]
                    self.list[left] = temp
            elif self.heapType == 'Max':
                if self.list[left] > self.list[right]:
                    swap = left
                else:
                    swap = right
                if self.list[index] < self.list[swap]:
                    temp = self.list[index]
                    self.list[index] = self.list[swap]
                    self.list[swap] = temp
            self.heapifyTreeExtract(swap)

    def extractNode(self):
        if self.heapSize == 0:
            return
        else:
            extractedNode = self.list[1]
            self.list[1] = self.list[self.heapSize]
            self.list[self.heapSize] = None
            self.heapSize -= 1
            self.heapifyTreeExtract(1)
            return extractedNode

    def delHeap(self):
        self.list = [None] * self.maxSize


# h = Heap(7, "Max")
# h.insertNode(10)
# h.levelOrderTraversal()
# h.insertNode(30)
# h.levelOrderTraversal()
# h.insertNode(20)
# h.levelOrderTraversal()
# h.insertNode(40)
# h.levelOrderTraversal()
# h.insertNode(50)
# h.levelOrderTraversal()
# h.insertNode(60)
# h.levelOrderTraversal()
# h.insertNode(70)
# h.levelOrderTraversal()
# h.insertNode(80)
# h.levelOrderTraversal()
# print(h.extractNode())
# h.levelOrderTraversal()
