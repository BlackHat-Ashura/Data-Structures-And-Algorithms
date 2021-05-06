class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if not len(self.list):
            return None
        else:
            return self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enQueue(self, value):
        self.inStack.push(value)
        print(f"[+] Successfully added {value} to Queue.\n")

    def deQueue(self):
        while self.inStack:
            self.outStack.push(self.inStack.pop())
        value = self.outStack.pop()
        while self.outStack:
            self.inStack.push(self.outStack.pop())
        return value


# QS = QueueViaStack()
# QS.enQueue(1)
# QS.enQueue(2)
# QS.enQueue(3)
# QS.enQueue(4)
# QS.enQueue(5)
# print(QS.deQueue())
# print(QS.deQueue())
# print(QS.deQueue())
