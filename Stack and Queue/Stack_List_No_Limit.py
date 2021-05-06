class Stack:
    def __init__(self):
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

    def push(self, value):
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


# S = Stack()
# S.push(3)
# S.push(2)
# S.push(1)
# print(S, "\n===")
# S.pop()
# print(S)
# S.peek()
# S.delStack()
# S.peek()
