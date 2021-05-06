class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.isEmpty():
            return "[!] Queue is empty.\n"
        else:
            values = [str(value) for value in self.list]
            return 'Out<- ' + ' '.join(values) + ' <-In\n'

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def enQueue(self, value):
        self.list.append(value)
        print(f"[+] Successfully added {value} to Queue.\n")

    def deQueue(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            first = self.list[0]
            self.list = self.list[1:]
            return first

    def peek(self):
        if self.isEmpty():
            print("[!] Queue is empty.\n")
        else:
            print(f"[+] First in Queue = {self.list[0]}\n")

    def delQueue(self):
        self.list = []
        print("[+] Successfully deleted Queue.\n")


# Q = Queue()
# Q.enQueue(3)
# Q.enQueue(2)
# Q.enQueue(1)
# print(Q)
# Q.deQueue()
# print(Q)
# Q.peek()
# Q.delQueue()
# Q.peek()
