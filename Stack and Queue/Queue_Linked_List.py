class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode.value
            tempNode = tempNode.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return "[!] Queue is empty.\n"
        else:
            values = [str(value) for value in self.LinkedList]
            return 'Out<- ' + ' '.join(values) + ' <-In\n'

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def enQueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
            print(f"[+] Successfully added {value} to Queue.\n")
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
            print(f"[+] Successfully added {value} to Queue.\n")

    def deQueue(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            if self.LinkedList.head is None:
                self.LinkedList.tail = None
            return value

    def peek(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            print(f"[+] First in Queue = {self.LinkedList.head.value}\n")

    def delQueue(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
        print("[+] Successfully deleted Queue.\n")


# Q = Queue()
# Q.enQueue(1)
# Q.enQueue(2)
# Q.enQueue(3)
# print(Q)
# Q.deQueue()
# print(Q)
# Q.enQueue(4)
# print(Q)
# Q.enQueue(5)
# print(Q)
# Q.enQueue(6)
# print(Q)
# Q.deQueue()
# print(Q)
# Q.enQueue(7)
# print(Q)
# Q.deQueue()
# print(Q)
# Q.deQueue()
# print(Q)
# Q.deQueue()
# print(Q)
# Q.deQueue()
# print(Q)
