class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode.value
            tempNode = tempNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return "[!] Stack is empty.\n"
        else:
            values = [str(value) for value in self.LinkedList]
            return '=Top=\n|' + '|\n|'.join(values) + '|\n=Bottom=\n'

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        print(f"[+] Successfully added {value} to Stack.\n")

    def pop(self):
        if self.isEmpty():
            print("[!] Stack is empty.\n")
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            print("[!] Stack is empty.\n")
        else:
            print(f"[+] Top of Stack = {self.LinkedList.head.value}\n")

    def delStack(self):
        self.LinkedList.head = None
        print("[+] Successfully deleted Stack.\n")


# S = Stack()
# S.push(3)
# S.push(2)
# S.push(1)
# print(S,)
# S.pop()
# print(S)
# S.peek()
# S.delStack()
# S.peek()
