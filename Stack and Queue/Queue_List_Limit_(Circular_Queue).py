class Queue:
    def __init__(self, max_size):
        self.list = [None] * max_size
        self.max_size = max_size
        self.start = -1
        self.end = -1

    def __str__(self):
        if self.isEmpty():
            return "[!] Queue is empty.\n"
        else:
            if self.start <= self.end:
                values = self.list[self.start:self.end+1]
                values = [str(value) for value in values]
                return 'Out<- ' + ' '.join(values) + ' <-In\n'
            else:
                values = self.list[self.start:]
                values.extend(self.list[:self.end+1])
                values = [str(value) for value in values]
                return 'Out<- ' + ' '.join(values) + ' <-In\n'

    def isFull(self):
        if self.end + 1 == self.start:
            return True
        elif self.start == 0 and self.end + 1 == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("[!] Queue is full.")
            print(f"[-] Failed to add {value} to Queue.\n")
        else:
            if self.end + 1 == self.max_size:
                self.end = 0
            else:
                self.end += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.end] = value
            print(f"[+] Successfully added {value} to Queue.\n")

    def deQueue(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            value_position = self.start
            value = self.list[value_position]
            if self.start == self.end:
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.list[value_position] = None
            return value

    def peek(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            print(f"[+] First in Queue = {self.list[self.start]}\n")

    def delQueue(self):
        self.list = [None] * self.max_size
        self.start = -1
        self.end = -1
        print("[+] Successfully deleted Queue.\n")


# Q = Queue(4)
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
