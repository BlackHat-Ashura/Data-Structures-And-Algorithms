class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.custom_stack = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def print(self, stackNum):
        begin = (stackNum - 1) * self.stack_size
        end = self.indexOfTop(stackNum) + 1
        values = self.custom_stack[begin:end]
        values = values[::-1]
        values = [str(value) for value in values]
        print('=Top=\n|' + '|\n|'.join(values) + '|\n=Bottom=\n')

    def isFull(self, stackNum):
        if self.sizes[stackNum - 1] == self.stack_size:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if not self.sizes[stackNum - 1]:
            return True
        else:
            return False

    def indexOfTop(self, stackNum):
        offset = (stackNum - 1) * self.stack_size
        return offset + self.sizes[stackNum - 1] - 1

    def push(self, value, stackNum):
        if self.isFull(stackNum):
            print(f"[!] Stack {stackNum} is full.")
            print(f"[-] Failed to add {value} to Stack {stackNum}.\n")
        else:
            self.custom_stack[self.indexOfTop(stackNum) + 1] = value
            self.sizes[stackNum - 1] += 1
            print(f"[+] Successfully added {value} to Stack {stackNum}.\n")

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            print(f"[!] Stack {stackNum} is empty.\n")
        else:
            value = self.custom_stack[self.indexOfTop(stackNum)]
            self.sizes[stackNum - 1] -= 1
            return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            print(f"[!] Stack {stackNum} is empty.\n")
        else:
            print(f"[+] Top of Stack {stackNum} = {self.custom_stack[self.indexOfTop(stackNum)]}\n")


# MS = MultiStack(3)
# MS.push(1, 1)
# MS.push(2, 1)
# MS.push(3, 1)
# MS.push(4, 2)
# MS.push(5, 2)
# MS.pop(1)
# MS.push(6, 2)
# MS.push(7, 3)
# MS.push(8, 3)
# MS.push(9, 3)
# MS.pop(3)
# MS.print(1)
# MS.print(2)
# MS.print(3)
# MS.peek(2)
