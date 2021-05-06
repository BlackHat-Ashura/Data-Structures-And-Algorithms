class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.topNode = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            print("[!] Stack is empty.\n")
        else:
            print(f"[+] The minimum of stack is {self.minNode.value}.\n")

    def push(self, value):
        if self.minNode and (self.minNode.value < value):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=value, next=self.minNode)
        self.topNode = Node(value=value, next=self.topNode)
        print(f"[+] Successfully added {value} to Stack.\n")

    def pop(self):
        if not self.topNode:
            print(f"[!] Stack is empty.\n")
        else:
            value = self.topNode.value
            self.minNode = self.minNode.next
            self.topNode = self.topNode.next
            return value


# S = Stack()
# S.push(10)
# S.min()
# S.push(5)
# S.min()
# S.push(6)
# S.min()
# S.pop()
# S.min()
# S.pop()
# S.min()
# S.pop()
# S.min()
