class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        if self.isEmpty():
            return "[!] Stack is empty.\n"
        else:
            values = self.list[::-1]
            values = [str(value) for value in values]
            return '=Top=\n|' + '|\n|'.join(values) + '|\n=Bottom=\n'

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) is self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("[!] Stack is full.")
            print(f"[-] Failed to add {value} to Stack.\n")
        else:
            self.list.append(value)
            print(f"[+] Successfully added {value} to Stack.\n")

    def pop(self):
        if self.isEmpty():
            print("[!] Stack is empty.\n")
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print("[!] Stack is empty.\n")
        else:
            print(f"[+] Top of Stack = {self.list[len(self.list) - 1]}\n")

    def delStack(self):
        self.list = []
        print("[+] Successfully deleted Stack.\n")


# S = Stack(3)
# S.push(3)
# S.push(2)
# S.push(1)
# print(S, "\n===")
# S.pop()
# print(S)
# S.peek()
# S.delStack()
# S.peek()
